'''
This version of the publisher assumes that all clients can be connected to the same WiFi network.
'''
import zmq, sys, datetime, time

def main():

    ### Command Line Parsing ###
    if (len(sys.argv) != 3):
        sys.stderr.write("Usage: python3 publisher.py [num_ports] [client_no]\n")
        exit(1)
    num_ports = int(sys.argv[1])
    client_no = int(sys.argv[2])
    if (num_ports <= client_no): # client numbers should start from 0
        sys.stderr.write("Error: client number must be less than number of ports.\n")
        exit(1)

    ### Create Publisher Sockets ###
    print("Clients: %d\nClient Number: %d" %(num_ports, client_no))

    context = zmq.Context()
    port = 8888
    sock_arr = [0 for i in range(num_ports)]

    try:
        for i in range(len(sock_arr)):
            sock_arr[i] = context.socket(zmq.PUB)
            tcp_addr = "tcp://127.0.0.1:" + str(port)
            (sock_arr[i]).bind(tcp_addr)
            print("Bound to " + tcp_addr)
            port += 1

        ### Send Messages to Publisher ###
        while True:
            for sock in sock_arr:
                sock.send_string(str(datetime.datetime.now()))
            time.sleep(1)
    except KeyboardInterrupt:
        # Safe socket closing
        for sock in sock_arr:
            if (type(sock) != int): # the default type before init
                sock.close()
        print("Closing publisher...")
        exit(0)

def run():
    print("Publisher - ZMQ Based Sync System")
    main()

run()

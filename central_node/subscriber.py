'''
This version of the subscriber assumes that all clients can be connected to the same WiFi network.
'''
import zmq, sys, datetime, time
from file_io import *

def main():

    ### Command Line Parsing ###
    if (len(sys.argv) != 3):
        sys.stderr.write("Usage: python3 subscriber.py [client_no] [host_ip]\n")
        exit(1)
    client_no = int(sys.argv[1])
    host_ip = sys.argv[2]
    sock = 0

    ### Create Subscriber Sockets ###
    print("Client Number: %d" % client_no)

    try:
        context = zmq.Context()
        sock = context.socket(zmq.SUB)
        sock.setsockopt_string(zmq.SUBSCRIBE, "") # accepts messages with any prefix
        port = 8888 + client_no
        print("Connecting to port %d" % port)
        sock.connect("tcp://%s:%d" % (host_ip, port))

        print("\t  --- Server time --- | --- Client Time ---")
        while True:
            message = sock.recv()
            log = str(message) + " | " + str(datetime.datetime.now())
            print(log)
            writeFile("log.txt", "\n" + log)

    except KeyboardInterrupt:
        # Safe socket closing
        if (type(sock) != int): # it has been assigned socket
            sock.close()
        print("\nClosing sockets...")
        exit(0)

def run():
    print("Subscriber - ZMQ Based Sync System")
    main()

run()

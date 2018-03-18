'''
This version of the subscriber assumes that all clients can be connected to the same WiFi network.
'''
import zmq, sys, datetime, time
from file_io import *

def main():

    ### Command Line Parsing ###
    if (len(sys.argv) != 4):
        sys.stderr.write("Usage: python3 subscriber.py [num_ports] [client_no] [host_ip]\n")
        exit(1)
    num_ports = int(sys.argv[1])
    client_no = int(sys.argv[2])
    host_ip = sys.argv[3]
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
            curr_time = str(datetime.datetime.now())
            log = str(message) + " | " + curr_time

            # Extract seconds from datetime
            split_time = (curr_time.split("."))[0]
            sec = int(split_time[len(split_time) - 2: len(split_time)])

            if (sec % num_ports == client_no):
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

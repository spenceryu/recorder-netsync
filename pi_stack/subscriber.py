'''
This version of the subscriber assumes that not all clients can be connected to the same WiFi network. It alternates the connected wifi network based on the current time.
'''
import zmq, sys, datetime, time
from file_io import *
from wifi import *

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

        while True:
            ### Using wifi module, connect to appropriate network ###
            # https://wifi.readthedocs.io/en/latest/
            # https://stackoverflow.com/questions/20470626/python-script-for-raspberrypi-to-connect-wifi-automatically
            ### if (time condition satisfied):
                ### Create a socket ###
                sock = context.socket(zmq.SUB)
                sock.setsockopt_string(zmq.SUBSCRIBE, "") # accepts messages with any prefix
                port = 8888 + client_no
                print("Connecting to port %d" % port)
                sock.connect("tcp://%s:%d" % (host_ip, port))

                print("\t  --- Server time --- | --- Client Time ---")

                ### while (time condition satisfied):
                    ### Receive data ###
                    message = sock.recv()
                    curr_time = str(datetime.datetime.now())
                    log = str(message) + " | " + curr_time

                    ### Extract seconds from datetime ###
                    split_time = (curr_time.split("."))[0]
                    sec = int(split_time[len(split_time) - 2: len(split_time)])

                    if (sec % num_ports == client_no):
                        print(log)
                        writeFile("log.txt", "\n" + log)

                ### Close the socket and reset the sock identifier ###
                for sock in sock_arr:
                    if (type(sock) != int):
                        sock.close()
                        sock = 0
                print("\nClosing sockets...")

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

# https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library
# https://stackoverflow.com/questions/14713711/zeromq-multiple-publishers-and-listener
import zmq
import sys
from datetime import datetime

## To run script ##
# % python3 script.py <node_id>

# Use this to distribute the socket to connect to
try:
    node_id = int(sys.argv[0]) # used to create "offset" in ports
    print("NODE # %d initialized" % node_id)
except:
    sys.exit("No arguments given, specify node number.")

# ZeroMQ Context
context = zmq.Context()
sock_port = 5670 + node_id
sock = context.socket(zmq.PAIR)
host_tcp_ip = "tcp://127.0.0.1:" + str(sock_port) # HOST port
sock.connect(host_tcp_ip)

# Send a "message" using the socket
# TODO: set up a timer for this
sock.send_string("Client %d connected" % node_id)

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)

while True:
    server_time = str(sock.recv())
    write = "server: " + server_time + " | sys: " + str(datetime.now())
    print(write)
    writeFile("log.txt", write + "\n")


# https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library
# https://stackoverflow.com/questions/14713711/zeromq-multiple-publishers-and-listener
import zmq
import sys
from datetime import datetime

# Use this to distribute the socket to connect to
args = sys.argv
num_nodes = sys.argv[0]
node_id = sys.argv[1]

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
#sock = context.socket(zmq.REQ) # blocked until response recv
sock = context.socket(zmq.PAIR)
sock.connect("tcp://127.0.0.1:5670")

# Send a "message" using the socket
# TODO: set up a timer for this
#sock.send(" ".join(sys.argv[1:]))
sock.send_string("Client connected")

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)

while True:
    local_time = str(datetime.now())
    write = "server: " + str(sock.recv()) + " | sys: " + local_time
    print(write)
    writeFile("log.txt", write + "\n")


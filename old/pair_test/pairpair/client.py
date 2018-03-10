import zmq
import sys
from datetime import datetime

# Node ID
try:
    num_nodes = sys.argv[0]
    node_id = sys.argv[1]
except:
    pass

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PAIR)
sock.connect("tcp://127.0.0.1:5670")

# Send a "message" using the socket
sock.send_string("Client connected")

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


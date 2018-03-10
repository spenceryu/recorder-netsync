'''
Old version of file - this contains useful snippets to integrate into main
'''

### SERVER ###
import sys
import zmq
from datetime import datetime
import _thread
import time

# Use this to distribute the socket to connect to
try:
    node_id = int(sys.argv[1])
    if (node_id < 1):
        sys.exit("node_id must be at least 1")
    num_nodes = int(sys.argv[2])
    if (num_nodes < 2):
        sys.exit("There must be at least two nodes")
except:
    sys.exit("Usage: % python3 <filename.py> <node_id> <num_nodes>")

print("Server started: NODE %d" % node_id)

# Server socket
context = zmq.Context()
sock = context.socket(zmq.PAIR)
port = 5670 + node_id
print("Connecting to port %d" % port)
sock.bind("tcp://127.0.0.1:" + str(port))
print("SERVER socket bound")

# Connect a client to node_id - 1
if (node_id > 1):
    context1 = zmq.Context()
    sock1 = context1.socket(zmq.PUB)
    sock1.connect("tcp://127.0.0.1:" + str(port - 1))
    sock1.send_string("Node %d connected as a client to node %d" % (node_id, node_id - 1))

### Useful Functions ###

def readFile(path):
    with open(path, "r") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)

def sendTime():
    # sends time from lower node to higher node number (ie sock -> other sock1)
    sock.send_string(str(datetime.now()))
    print("Sent time")

###########################

def sock_recv():
    message = str(sock.recv())
    print("Recv: " + message + "at" + str(datetime.now()))
    writeFile("log.txt", message + "\n")

def safe_send_time():
    try:
        sendTime()
    except:
        print("No node connected: time not sent")

while True:
    time.sleep(1) # seconds
    print("Polling...")
    _thread.start_new_thread(sock_recv, ()) # this might cause overloading if never recv
    _thread.start_new_thread(safe_send_time, ())

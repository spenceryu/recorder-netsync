import zmq, sys
from datetime import datetime
# proof of concept

try:
    node_id = sys.argv[1]
    print("NODE %s" % node_id)
except:
    raise Exception("Error: python3 <file> <node_id> : node_id = 0 or 1")

# set up zmq socket
context = zmq.Context()
# we want this to be sending out messages and waiting for a response
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:8889")
sock.send_string("Client %s connected" % node_id)
print("Sent: 'Client %s connected'" % node_id)
print(sock.recv())

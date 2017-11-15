# https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library
import zmq
import sys
from datetime import datetime

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
#sock = context.socket(zmq.REQ) # blocked until response recv
sock = context.socket(zmq.PAIR)
sock.connect("tcp://127.0.0.1:5678")

# Send a "message" using the socket
# TODO: set up a timer for this
#sock.send(" ".join(sys.argv[1:]))
msg = str(datetime.now())
sock.send_string("hi")

print(sock.recv())

count = 0
while True:
    count += 1
    sock.send_string("HI %d" % count)

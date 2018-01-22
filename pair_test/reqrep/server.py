import zmq, sys
from datetime import datetime
# proof of concept

print("SERVER LOADED")
# set up zmq socket
context = zmq.Context()
# we want this to be receiving messages and echoing the message back
sock = context.socket(zmq.REP)
sock.connect("tcp://127.0.0.1:8889")

while True:
    message = sock.recv()
    print("ECHO: " + str(message))
    sock.send_string("echo: " + message)

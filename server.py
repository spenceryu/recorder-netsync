import zmq
from datetime import datetime
from threading import Timer

print("Server started")

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
# sock = context.socket(zmq.REP) # block on recv unless it has recv'd requests
sock = context.socket(zmq.PAIR)
sock.bind("tcp://127.0.0.1:5670")
print("Socket bound")

def sendTime():
    sock.send_string(str(datetime.now()))
    print("Sent time")
    t = Timer(interval, sendTime)
    t.start()

interval = 1
t = Timer(interval, sendTime)
print("Timer created: %d second interval" % interval)
t.start()

while True:
    message = sock.recv()
    #sock.send_string(str(datetime.now()))
    print("Recv: " + str(message))

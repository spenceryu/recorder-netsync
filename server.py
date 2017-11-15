import zmq
from datetime import datetime

print("Server started")

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
# sock = context.socket(zmq.REP) # block on recv unless it has recv'd requests
sock = context.socket(zmq.PAIR)
sock.bind("tcp://127.0.0.1:5678")
print("Socket bound")

# Run a simple "Echo" server
while True:
    message = sock.recv()
    #sock.send("Echo: " + message)
    #print(str(datetime.now()))
    sock.send_string("Echo: " + str(message))
    #sock.send_string(str(datetime.now()))
    print("Recv: " + str(message))

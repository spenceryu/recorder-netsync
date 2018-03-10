import zmq

# this one doesn't work b/c router not configured correctly
context = zmq.Context()
sock = context.socket(zmq.ROUTER)
sock.bind("tcp://127.0.0.1:0000")

try:
    while True:
        message = sock.recv()
        print(message)
        sock.send_string(message)
except:
    sock.close()

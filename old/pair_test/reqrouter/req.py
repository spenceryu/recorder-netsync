import zmq

# this one doesn't work because req not configured correctly
context = zmq.Context()
sock = context.socket(zmq.REQ)
sock.bind("tcp://127.0.0.1:0000")

try:
    while True:
        sock.send_string("hi")
except:
    sock.close()

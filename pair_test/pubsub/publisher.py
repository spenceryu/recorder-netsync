import zmq

context = zmq.Context()
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:8888")

while True:
    sock.send_string("message from publisher")

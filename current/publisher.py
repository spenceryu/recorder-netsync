import zmq

context = zmq.Context()
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:8888") # sudo ifconfig to find IP address of the host pi

while True:
    sock.send_string("message from publisher")

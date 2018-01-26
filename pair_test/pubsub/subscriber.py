import zmq

context = zmq.Context()
sock = context.socket(zmq.SUB)
sock.setsockopt_string(zmq.SUBSCRIBE, "") # accepts messages with any prefix
sock.connect("tcp://127.0.0.1:8888")

while True:
    message = sock.recv()
    print(message)

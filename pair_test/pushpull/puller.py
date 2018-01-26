import zmq

context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.bind("tcp://127.0.0.1:10000")

try:
    while True:
        message = sock.recv()
        print(message)
except KeyboardInterrupt:
    print("close...")
    sock.close()

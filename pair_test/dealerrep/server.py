import zmq

context = zmq.Context()
sock = context.socket(zmq.DEALER)
sock.bind('tcp://127.0.0.1:7888')

try:
    while True:
        message = sock.recv()
        sock.send_string("message recv")
except:
    sock.close()

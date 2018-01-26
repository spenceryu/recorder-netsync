import zmq

context = zmq.Context()
sock = context.socket(zmq.REP)
sock.bind('tcp://127.0.0.1:7888')

sock.send_string("client connected")
sock.close()

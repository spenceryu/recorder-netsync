import zmq
# pipeline pattern.. items queued -> users demand (pull)

context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:10000")

try:
    while True:
        sock.send_string("hi")
except KeyboardInterrupt:
    print("close...")
    sock.close()

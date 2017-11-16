# Python/Sockets message sending

# Functionality
- Distributed message passing
- Set time on each Raspberry Pi
- Record local time (on pi) and receieved time (network), log to .txt file
- Multiprocessing (later) for increased speed

# Calculate delta between local and received time

## Design
- zmq.PAIR: allows for messages without a reply

# recorder-netsync
Synchronization software for CMU Navlab traffic recording boxes (Python 3)

% pip3 install zmq

% python3 client.py

% python3 server.py

# Functionality
- Distributed message passing
- Set time on each Raspberry Pi
- Record local time (on pi) and receieved time (network), log to .txt file
- Calculate delta between local and received time

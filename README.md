# recorder-netsync
Synchronization software for CMU Navlab traffic recording boxes (Python 3)

# Installation on Mac:
pip3 install zmq; python3 client.py; python3 server.py

# Installation on Raspberry Pi:
- Setting up zmq: chmod 755 install.sh; ./install.sh
- For the publisher device: https://cdn-learn.adafruit.com/downloads/pdf/setting-up-a-raspberry-pi-as-a-wifi-access-point.pdf
- If using an external antenna on the publisher: replace wlan0 with wlan1 in all the configuration files. Also, the driver might have to be changed from the default one to another driver listed in the adafruit pdf.

# Functionality
- Distributed message passing
- Set time on each Raspberry Pi
- Record local time (on pi) and receieved time (network), log to .txt file

# Errors?
External adapter + the wifi AP is not started? ./runservice.sh 
Make sure the host IP that is being used in the publisher.py or subscriber.py files is not 127.0.0.1 or localhost.

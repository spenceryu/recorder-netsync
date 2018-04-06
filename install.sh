#!/bin/bash
# Run "chmod 755 install.sh" to grant write, modify, execute
# run this on raspberry pi
# https://github.com/MonsieurV/ZeroMQ-RPi

sudo apt-get install libtool pkg-config build-essential autoconf automake

wget https://github.com/jedisct1/libsodium/releases/download/1.0.3/libsodium-1.0.3.tar.gz
tar -zxvf libsodium-1.0.3.tar.gz
cd libsodium-1.0.3/
./configure
make
sudo make install

wget http://download.zeromq.org/zeromq-4.1.3.tar.gz
tar -zxvf zeromq-4.1.3.tar.gz
cd zeromq-4.1.3/
./configure
make
sudo make install
sudo ldconfig

sudo apt-get install python-dev
sudo pip install pyzmq

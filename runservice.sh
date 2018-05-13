#!/bin/bash
# Run "chmod 755 runservice.sh" to grant write, modify, execute
# run this on raspberry pi
# https://github.com/MonsieurV/ZeroMQ-RPi
#
# This script runs the access point manually on Raspberry Pi.

sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf

#!/bin/bash
# Run "chmod 755 get_ip.sh" to grant write, modify, execute

echo Getting ip address of device... most likely 192.168.x.x
sudo ifconfig | grep "inet addr"

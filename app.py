#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
# Meteostation connector
# Title: Connector which gets data via USB/serial and parse data and after that send it to the cloud
# Author: Vojtěch Petrásek
# Generated: 21/2/2023 13:40:01
##################################################

###
# imports
###

import os
import sys
import time
import serial
import serial.tools.list_ports

###
# get com ports
###

def get_com_ports():
    return [p.device for p in serial.tools.list_ports.comports()]

###
# select port
###

def select_and_open_port(com_ports):
    for i in range(len(com_ports)):
        print(i,com_ports[i])
    selected_com_port = int(input("please select COM port of meteostation: "))
    ser = serial.Serial(com_ports[selected_com_port], 115200)
    return ser
###
# main
###

def main():
    com_ports = get_com_ports()

    if len(sys.argv) > 1:
        if sys.argv[1] in com_ports:
            ser = serial.Serial(sys.argv[1], 115200)
        else:
            ser = select_and_open_port(com_ports)
    else:
        ser = select_and_open_port(com_ports)

    while(ser.is_open):
        try:
            print(ser.readline())
        # except TypeError:
        except Exception as e:
            print("bad read")
            break





if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Exited with error: {}'.format(e))
        sys.exit(1)
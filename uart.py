# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:50:17 2022

@author: hjw
"""

import serial
import sys
import time

def port_available():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    print(result)
    return result


def send(data_s,port_num,baudrate):
    ser = serial.Serial(port_num,baudrate)
    data_s = bytearray(str(data_s), encoding="utf-8")
    ser.write(data_s)
    return data_s


def receive(port_num,baudrate):
    ser = serial.Serial(port_num,baudrate)
    while 1:
        if ser.inWaiting():
            data_r = ser.readall()
            return data_r
        else:
            time.sleep(0.01)
    
    


data = 'AAAA'
port_num = 'COM2'
baudrate = 115200

send(data,port_num,baudrate)
receive(port_num,baudrate)

# -*- coding: utf-8 -*-
import serial
from time import sleep

sw_open = 0xA0, 0x01, 0x01, 0xA2  # sw open
sw_close = 0xA0, 0x01, 0x00, 0xA1  # sw close


def key_open():
    s = serial.Serial("/dev/ttyUSB0", 9600)
    s.write(sw_open)
    sleep(0.35)
    s.write(sw_close)
    sleep(0.35)
    s.close()


def main():
    key_open()


if __name__ == "__main__":
    main()

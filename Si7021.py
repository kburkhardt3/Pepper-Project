#!/usr/bin/env python3

import smbus
import time

def Si7021():

    bus = smbus.SMBus(1) # I2C bus
    address = 0x40 # Si7021 address
    hum = 0xF5 # measure relative humidity command
    temp = 0xE0 # read temperature from humidity command
    # NB: temperature is read with humidity to get relative
    # humidity, temperature need not be measured again
    
    bus.write_byte(address, hum) # measure hum and temp
    time.sleep(0.1)

    msbyte = bus.read_byte(address)
    lsbyte = bus.read_byte(address)

    humidity = ((msbyte*256+lsbyte)*125/65536)-6

    bus.write_byte(address, temp) # recalls temp
    time.sleep(0.1)

    msbyte = bus.read_byte(address)
    lsbyte = bus.read_byte(address)

    cTemp = ((msbyte*256+lsbyte)*175.72/65536)-46.85
    fTemp = cTemp*1.8+32

    return humidity, fTemp

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
import datetime

hour = int(datetime.datetime.now().strftime(¨%H¨))

t_on =
t_off = 

on = True
off = False

fan = 0 # BCM pin number
led_strand = 5
led_board = 6
bulb = 13

GPIO.setup(fan, GPIO.OUT) # define pins as output
GPIO.setup(led_strand, GPIO.OUT)
GPIO.setup(led_board, GPIO.OUT)
GPIO.setup(bulb, GPIO.OUT)

GPIO.output(fan, on) # fan always on

(humidity, temperature) = Si7021()

if temperature < 80:
    GPIO.output(bulb, on)
else:
    GPIO.output(bulb, off)
   
if hour > t_on and hour < t_off: # on between t_on and t_off
    GPIO.output(led_strand, on)
    GPIO.output(led_board, on)
else: # off before t_on and after t_off
    GPIO.output(led_strand, off)
    GPIO.output(led_board, off)

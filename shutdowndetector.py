#!/bin/python3

#######################################
# RPi button shutdown detector
#
# Taka Kitazume
# Version 0.1
# December 29, 2020
#######################################

import RPi.GPIO as GPIO
import time
import os

PIN_SHUTDOWN = 3
BUTTON_SECONDS = 3

GPIO.setmode(GPIO.BCM)
# Do not set pull_up_down parameter if PIN 3 is used as a physical pull up resistor is fitted
GPIO.setup(PIN_SHUTDOWN, GPIO.IN)

print('Shutdown detector started')

def shutdown(channel):
    print('Shutdown button detected')

    # When button is pressed, GPIO.input(PIN_SHUTDOWN) is 0
    state = 0

    # Shutdown system if the button is pressed for BUTTON_SECONDS seconds or longer.
    current = time.monotonic_ns()/1000000000
    end     = current + (BUTTON_SECONDS)

    #print('CURRENT = {}'.format(current))
    #print('END     = {}'.format(end))

    while (current<end and state==0):
        current = time.monotonic_ns()/1000000000
        state=GPIO.input(channel)

        # print('UPDATED = {}'.format(current))
        # print('STATE   = {}'.format(state))
        # time.sleep(0.5)

    # Now check the state and if 0, then shutdown the device
    if state == 0:
        print('Shutdown process starts now.')
        os.system('sudo shutdown -h now')
    else:
        print('Shutdown process cancelled.')

GPIO.add_event_detect(PIN_SHUTDOWN, GPIO.FALLING, callback=shutdown, bouncetime=BUTTON_SECONDS * 1000)

try:
    while True:
        time.sleep(1)
except:
    print('Shutdown detector exception. Something went wrong')

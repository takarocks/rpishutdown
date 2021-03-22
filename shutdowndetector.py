#!/bin/python3

#######################################
# RPi button shutdown detector
#
# Taka Kitazume
# Version 0.2
# March 1, 2021
#######################################

import RPi.GPIO as GPIO
import time
import os
import requests

PIN_SHUTDOWN = 3
BUTTON_SECONDS = 3
SSD1306 = False

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

        print("inside while loop, GPIO.input(channel) = {}".format(GPIO.input(channel)))

        if SSD1306:
            sec = round(end - current)
            if sec < 0:
                sec = 0
            text = "Shutdown in {} seconds".format(sec)
            r = requests.get('http://localhost:5000/showmessage?text=' + text)
            time.sleep(1.1)

        # print('UPDATED = {}'.format(current))
        # print('STATE   = {}'.format(state))
        # time.sleep(0.5)

    # Now check the state and if 0, then shutdown the device
    if state == 0:
        text = 'Shutdown process starts now.'
        print(text)
        if SSD1306:
            r = requests.get('http://localhost:5000/showmessage?text=' + text)
        os.system('sudo shutdown -h now')
    else:
        text = 'Shutdown cancelled.'
        print(text)
        if SSD1306:
            r = requests.get('http://localhost:5000/showmessage?text=' + text)
            time.sleep(1)
            r = requests.get('http://localhost:5000/showmessage?text= ')

GPIO.add_event_detect(PIN_SHUTDOWN, GPIO.FALLING, callback=shutdown, bouncetime=BUTTON_SECONDS * 1000)

try:
    while True:
        time.sleep(1)
except:
    print('Shutdown detector exception. Something went wrong')

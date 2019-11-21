import RPi.GPIO as GPIO
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
nivel = GPIO.input(channel)
def som(nivel): # decibeis

    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, som)  # assign function to GPIO PIN, Run function on change
    return nivel


def led(): # ai liga on/off no cayanne
    if som(nivel) > 100:
        return 'ON'
    else:
        return 'OFF'

#!/usr/bin/python


#GPIO SETUP


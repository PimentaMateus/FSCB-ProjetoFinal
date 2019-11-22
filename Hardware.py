import RPi.GPIO as GPIO

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def sensor():
    return 1 if GPIO.input(channel) else 0


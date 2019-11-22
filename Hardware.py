import RPi.GPIO as GPIO

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def sensor():
    """funcao para o sensor de som"""
    return 1 if GPIO.input(channel) else 0

def led():
    """funcao para o LED"""
    return "LEDON" if GPIO.input(channel_led) else "LEDOFF"


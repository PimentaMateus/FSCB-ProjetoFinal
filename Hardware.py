import RPi.GPIO as GPIO
import Main
pinLED = 4
pinSensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSensor, GPIO.IN)
GPIO.setup(pinLED, GPIO.OUT)




def sensor():
    """funcao para o sensor de som"""
    return 1 if GPIO.input(pinSensor) else 0


def led():
    return GPIO.output(pinLED, GPIO.HIGH)

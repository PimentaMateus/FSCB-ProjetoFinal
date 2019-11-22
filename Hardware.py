import RPi.GPIO as GPIO
pinLED = 18
pinSensor = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSensor, GPIO.IN)
GPIO.setup(pinLED, GPIO.OUT)


def sensor():
    """funcao para o sensor de som"""
    return 1 if GPIO.input(pinSensor) else 0


def led():
    if sensor() > 0:
        return GPIO.output(pinLED, GPIO.HIGH)
    else:
        return GPIO.output(pinLED, GPIO.HIGH)

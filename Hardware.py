import RPi.GPIO as GPIO
pinLED = 22
pinSensor = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSensor, GPIO.IN)
GPIO.setup(pinLED, GPIO.OUT)




def sensor():
    if GPIO.input(pinSensor):
        led(1)
        return 1
    else:
        led(0)
        return 0
    #return 1 if GPIO.input(pinSensor) else 0


def led(status):
    if status == 1:
        return GPIO.output(pinLED, GPIO.HIGH)
    elif status == 0:
        return GPIO.output(pinLED, GPIO.LOW)
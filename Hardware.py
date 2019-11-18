'Aqui vamos fazer toda a camada de hardware, tudo que entra de valores do sensor e tudo que sai para o LCD e Buzzer.'
import RPi.GPIO as gpio
import time
pinoSom = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinoSom, GPIO.IN)

#Leitura do sensor de som
def detec(pinoSom):
    if GPIO.input(pinoSom):
        print("som...som")
    else:
        print("sem som...")


GPIO.addEventoDetec(pinoSom, GPIO.BOTH, bouncetime=300)
GPIO.addEventoCallBack(pinoSom, detec)


while True:
    time.sleep(1)

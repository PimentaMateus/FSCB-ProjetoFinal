import paho.mqtt.client as mqtt
import time
from Hardware import sensor
from Hardware import led

user = '7f730680-0734-11ea-b49d-5f4b6757b1bf'
password = 'dfb9be8e000efe3b25a1ae8885c4e16e0f2708e7'
client_id = '3718a860-0737-11ea-a38a-d57172a4b4d4'
server = 'mqtt.mydevices.com'
port = 1883

# Client ID
client = mqtt.Client(client_id)

# MQTT username, MQTT password
client.username_pw_set(user, password)

# MQTT Server, MQTT Port,
client.connect(server, port)

def detectasom1s():
    vezes = 0
    for x in range(100):
        time.sleep(.01)
        vezes += sensor()
        led()

    return 'Som Detectado' if vezes > 0 else 'Nada Detectado'


while True:
    client.publish('v1/' + user + '/things/' + client_id + '/data/1', detectasom1s())
    som = detectasom1s()
    print(som)





import socket
import paho.mqtt.client as mqtt

# FIXME: move hostname string into env variables
IPADDRESS = socket.gethostbyname('webserver')
MQTT_HOST = IPADDRESS
# FIXME: move port number into env variables
MQTT_PORT = 3001
MQTT_KEEPALIVE_INTERVAL = 60

def connect_mqtt():
    client = mqtt.Client()
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    return client
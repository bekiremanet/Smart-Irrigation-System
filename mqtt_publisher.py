import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import sys
import time
import dht11
import datetime

client = paho.Client()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    
    if result.is_valid():
	    print("Temperature: %-3.1f C" % result.temperature)
	    print("Humidity: %-3.1f %%" % result.humidity)
    

    if (client.connect("localhost", 1883, 60) != 0):
        print("Could not connect to MQTT Broker")
        sys.exit(-1)

    client.publish("temperature", str(result.temperature) + " Degree ", 0)
    time.sleep(5)
    client.publish("humidity", str(result.humidity) + " % " , 0)
    time.sleep(10)

client.disconnect()

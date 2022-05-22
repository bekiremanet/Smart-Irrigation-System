import paho.mqtt.client as paho
import RPi.GPIO as GPIO 
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

GPIO.setup(12,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)

def onMessage(client,userdata, msg):
    
    if "R1 ON" in msg.payload:
        #print(" Relay 1 on! ")
        GPIO.output(11, False)
    elif "R1 OFF" in msg.payload: 
        #print(" Relay 1 off! ")
        GPIO.output(11, True)
    elif "R2 ON" in msg.payload:
        #print(" Relay 1 on! ")
        GPIO.output(12, False)
    elif "R2 OFF" in msg.payload: 
        #print(" Relay 1 off! ")
        GPIO.output(12, True)
    elif "R3 ON" in msg.payload:
        #print(" Relay 1 on! ")
        GPIO.output(13, False)
    elif "R3 OFF" in msg.payload: 
        #print(" Relay 1 off! ")
        GPIO.output(13, True)
    elif "R4 ON" in msg.payload:
        #print(" Relay 1 on! ")
        GPIO.output(15, False)
    elif "R4 OFF" in msg.payload: 
        #print(" Relay 1 off! ")
        GPIO.output(15, True)

        
client = paho.Client()
client.on_message = onMessage


if (client.connect("localhost", 1883, 60) != 0):
    print("Could not connect to MQTT Broker")
    sys.exit(-1)

client.subscribe("valfControl")

try: 
    print("Press CTRL+C to exit...")
    client.loop_forever()
except: 
    print("Disconnecting from broker")

client.disconnect()



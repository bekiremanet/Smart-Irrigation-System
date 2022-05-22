# Smart-Irrigation-System

Smart Irrigation System w/MQTT &amp; RPi4.


In this study, Smart Irrigation system was simulated. MQTT protocol was used in the project. 
MQTT Broker is built on Raspberry PI.

Units that perform Publisher and Subscriber functions are also available on the Raspberry PI.


Installation steps are given below.

Before installing the MQTT broker to our Raspberry Pi, we need to update the operating system.
```
sudo apt update
sudo apt upgrade 
```

Once the system has finished updating, we can now install the Mosquitto software.
```
sudo apt install -y mosquitto mosquitto-clients
```

When the system is turned on, the following procedure is done for Mosquitto to run as well.
```
sudo systemctl enable mosquitto
```

Mosquitto Installation Check & Version Control.
```
mosquitto -v
```

Subscribe to "temperature" topic.
```
mosquitto_sub -d -t temperature
```
Subscribe to "humidity" topic.
```
mosquitto_sub -d -t humidity
```
Subscribe to "humidity" topic.
```
mosquitto_sub -d -t relayStatus
```






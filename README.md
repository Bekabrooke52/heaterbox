# Heater box

Hardware
* [JBtek 4 Channel DC 5V Relay](https://www.amazon.com/JBtek-Channel-Module-Arduino-Raspberry/dp/B00KTEN3TM/ref=sr_1_3)
* [DHT11 Temperature and Humidity Sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_8)

This Python script, heater-controller.py, provides a solution for controlling a relay-based heater system using temperature readings from a DHT11 sensor. The system is designed to maintain a desired temperature by turning the heater on or off based on a predefined threshold.

This Python script, heater-limits.py, is designed to control a heater and a fan based on ambient temperature readings from a DHT11 sensor. It continuously monitors the temperature and activates or deactivates the connected relays (for the heater and fan) to maintain the temperature within a specified range. If the temperature rises above an upper limit (20°C), both the heater and fan are turned off. Conversely, if the temperature drops below a lower limit (19°C), both the heater and fan are turned on. The script includes error handling for sensor readings and ensures proper GPIO cleanup upon termination.

Features
* Temperature Monitoring: Reads temperature data from a DHT11 sensor connected to a specified GPIO pin.
* Relay Control: Activates or deactivates a relay connected to another GPIO pin based on the measured temperature.
* Configurable Threshold: Easily adjust the temperature threshold at which the relay should switch.
* Error Handling: Includes retry mechanisms for DHT11 sensor readings to improve reliability.
* GPIO Cleanup: Ensures proper cleanup of GPIO settings upon program termination.

Run code
```
sudo python3 heater-controller.py
```

Run code
```
sudo python3 heater-limits.py
```

## Live Setup
![Live setup](https://github.com/rbm0622/heaterbox/blob/main/images/live-setup.jpeg?raw=true)

## Wiring Diagram
![heaterbox wireframe](https://github.com/rbm0622/heaterbox/blob/main/images/Heater-Box.jpg?raw=true)

## GPIO Pin Mapping
![GPIO Pin Map](https://github.com/rbm0622/heaterbox/blob/main/images/pinmapping.jpeg?raw=true)

## Diagram with Heater and Fan (WIP)
![heaterbox wireframe with heater and fan](https://github.com/rbm0622/heaterbox/blob/main/images/Heater-Box-WIP.jpg?raw=true)

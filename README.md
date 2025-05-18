# Heater box

Hardware
* JBtek 4 Channel DC 5V Relay
* DHT11 Temperature and Humidity Sensor

This Python script, heater-controller.py, provides a solution for controlling a relay-based heater system using temperature readings from a DHT11 sensor. The system is designed to maintain a desired temperature by turning the heater on or off based on a predefined threshold.

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

![heaterbox](https://github.com/user-attachments/assets/2a5f0ab4-2abe-415a-aa5d-fd371371f66a)

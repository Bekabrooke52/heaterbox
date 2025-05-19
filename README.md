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

## Live Setup
![heaterbox](https://github.com/user-attachments/assets/2a5f0ab4-2abe-415a-aa5d-fd371371f66a)

## Wiring Diagram
![Heater Box](https://github.com/user-attachments/assets/a6543edc-1d04-49fb-80e9-72d3af53d4b4)

## GPIO Pin Mapping
![pinmapping](https://github.com/user-attachments/assets/fb4ac874-0601-4152-af74-935b5f818737)

## Diagam with Heater and Fan (WIP)
![Heater Box 1](https://github.com/user-attachments/assets/bf8721df-f7bb-4a8c-957d-b7e598095206)


# Filename: heater-control-w1thermsensor.py
# Author: Rebeka B Mendelsohn
# Created: 2025-05-28
# Description: Code to turn a relay on/off (heater/fan) based on temperature using a w1thermsensor



import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor, SensorNotReadyError
import time
import csv
from datetime import datetime

# Pin Definition
RELAY_PIN_HEATER = 23 # GPIO pin corresponding to heater relay control pin
RELAY_PIN_FAN = 18 # GPIO pin corresponding to fan relay control pin
RELAY_PIN_HEATER_1 = 24 # GPIO pin corresponding to second heater relay control pin
RELAY_PIN_FAN_1 = 25 # GPIO pin corresponding to second fan relay control pin
SENSOR_PIN = 4 # GPIO pin corresponding to the Sensor control pin

# Temperature threshold
TEMP_UPPER_LIMIT = 40 # Temperature in celsius (heater turns OFF above this)
TEMP_LOWER_LIMIT = 30 # Temperature in Celsius (heater turns ON below this)

# Log file path
LOG_FILE = 'temperature_log.csv' # Adjust title as needed

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering

# Set up both relay pins as outputs
GPIO.setup(RELAY_PIN_HEATER, GPIO.OUT)  # HEATER relay pin as output
GPIO.setup(RELAY_PIN_FAN, GPIO.OUT) # FAN relay pin as output

GPIO.output(RELAY_PIN_HEATER, GPIO.HIGH) # HEATER initialized to OFF
GPIO.output(RELAY_PIN_FAN, GPIO.HIGH) # FAN initialized to OFF

GPIO.setup(RELAY_PIN_HEATER_1, GPIO.OUT)  # Second HEATER relay pin as output
GPIO.setup(RELAY_PIN_FAN_1, GPIO.OUT)  # Second FAN relay pin as output

GPIO.output(RELAY_PIN_HEATER_1, GPIO.HIGH) # Second HEATER initialized to OFF
GPIO.output(RELAY_PIN_FAN_1, GPIO.HIGH) # Second FAN initialized to OFF

# Initialize the DS18B20 Temperature Sensor
sensor= W1ThermSensor()

def read_temperature():
# Reads the temperature from the 1-wire sensor
# Returns:
# float: Temperature in Celsius, or None (error)
   for i in range(5): # Retries up to 5 times
      try:
         temperature = sensor.get_temperature()
         if temperature is not None:
            return temperature
        else: 
            print('Sensor Error: Reading failed. Retrying...')
      except SensorNotReadyError: # Common error with this sensor, usually do to poorely established signal connection with the bread board. Can be fixed by adjusting the pins
         print('Sensor Error: Reading failed. Check sensor connection. Retrying...')
         time.sleep(2)
         pass
      return None

def log_temperature(temperature):
# Logs temperature with timestamps to CSV file.
# Args:
#   temperature(float): The temperature in Celsius
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, mode = 'a', newline= '') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f'{temperature:.2f}'])
    print(f'Logged: {timestamp}, {temperature:.2f}C')

def control_relay(temperature):
# Control the relay based on the given temperature
# Args:
#   temperature (float): The temperature in Celsius
    if temperature is not None:
        if temperature > TEMP_UPPER_LIMIT
            print(f'Temperature {temperature:.2f}C is above the threshold ({TEMP_UPPER_LIMIT})C. Turning Relay OFF')
            GPIO.output(RELAY_PIN_HEATER, GPIO.HIGH) # Turn HEATER relay OFF
            GPIO.output(RELAY_PIN_FAN, GPIO.LOW) # keep FAN relay ON
            GPIO.output(RELAY_PIN_HEATER_1, GPIO.HIGH) # Turn second HEATER relay OFF
            GPIO.output(RELAY_PIN_FAN_1, GPIO.LOW) # keep second FAN relay ON

        elif temperature < TEMP_LOWER_LIMIT:
            print(f'Temperature {temperature:.2f}C is below the threshold ({TEMP_LOWER_LIMIT})C. Turning Relay ON')    
            GPIO.output(RELAY_PIN_HEATER, GPIO.LOW) # Turn HEATER relay ON
            GPIO.output(RELAY_PIN_FAN, GPIO.LOW) # Keep FAN relay ON
            GPIO.output(RELAY_PIN_HEATER_1, GPIO.LOW) # Turn second HEATER relay ON
            GPIO.output(RELAY_PIN_FAN_1, GPIO.LOW) # Keep second FAN relay ON
        else:
            print(f'Temperature {temperature:.2f}C is within limits ({TEMP_LOWER_LIMIT}C - {TEMP_UPPER_LIMIT}C). Keep current state.')
    else:
        print('Error: Could not read temperature. Keeping relay state unchanged.')

def main():
# Main function, continously reads temperature and controls the relay
    try:
        while True:
            temperature = read_temperature()
            if temperature is not None:
                print(f'Temperature: {temperature:.2f}C')
                control_relay(temperature)
               log_temperature(temperature)
            else:
                print('Failed to read temperature')
               
            time.sleep(30)
    except KeyboardInterrupt:
        print('Program terminated by User.')
    finally:
        GPIO.cleanup() # Reset GPIO settings on exit
      
if __name__== '__main__':
   main()

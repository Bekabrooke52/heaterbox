# Filename: heater-limits.py
# Author: Rebeka B. Mendelsohn
# Created: 2025-05-27
# Description: Controller code that turns on / off a relay based on temperature
#              within specified upper and lower limits, now with two relay pins.

import RPi.GPIO as GPIO
import Adafruit_DHT  # Use Adafruit_DHT for DHT11
import time  # Import the time module

# Pin definitions
DHT11_PIN = 27         # GPIO pin connected to DHT11 data pin
RELAY_PIN_HEATER = 17  # GPIO pin connected to the heater relay control pin
RELAY_PIN_FAN = 4      # GPIO pin connected to the fan relay control pin

# Temperature limits
TEMP_UPPER_LIMIT = 20  # Temperature in Celsius (Heater turns OFF if above this)
TEMP_LOWER_LIMIT = 19  # Temperature in Celsius (Heater turns ON if below this)

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering

# Set both relay pins as outputs
GPIO.setup(RELAY_PIN_HEATER, GPIO.OUT)
GPIO.setup(RELAY_PIN_FAN, GPIO.OUT)

# Initialize both relays to OFF (normally open, HIGH for OFF)
GPIO.output(RELAY_PIN_HEATER, GPIO.HIGH)
GPIO.output(RELAY_PIN_FAN, GPIO.HIGH)

# Initialize DHT11 sensor
DHT_SENSOR = Adafruit_DHT.DHT11  # Define the sensor.


def read_temperature():
    """
    Reads the temperature from the DHT11 sensor using Adafruit_DHT.
    Handles retries and errors.
    Returns:
        float: Temperature in Celsius, or None on error.
    """
    for _ in range(5):  # Retry up to 5 times
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT11_PIN)
        if temperature is not None:
            return temperature
        else:
            print("DHT11 Sensor Error: Reading failed. Retrying...")
        time.sleep(2)
    return None


def control_relay(temperature):
    """
    Controls both relays based on the given temperature and defined limits.
    Args:
        temperature (float): The temperature in Celsius.
    """
    if temperature is not None:
        if temperature > TEMP_UPPER_LIMIT:
            print(
                f"Temperature {temperature:.2f}°C is above upper limit ({TEMP_UPPER_LIMIT}°C). Turning heater OFF and fan OFF."
            )
            # Turn heater OFF and fan OFF
            GPIO.output(RELAY_PIN_HEATER, GPIO.HIGH)
            GPIO.output(RELAY_PIN_FAN, GPIO.HIGH)
        elif temperature < TEMP_LOWER_LIMIT:
            print(
                f"Temperature {temperature:.2f}°C is below lower limit ({TEMP_LOWER_LIMIT}°C). Turning heater ON and fan ON."
            )
            # Turn heater ON and fan ON
            GPIO.output(RELAY_PIN_HEATER, GPIO.LOW)
            GPIO.output(RELAY_PIN_FAN, GPIO.LOW)
        else:
            print(
                f"Temperature {temperature:.2f}°C is within limits ({TEMP_LOWER_LIMIT}°C - {TEMP_UPPER_LIMIT}°C). Keeping current state."
            )
            # No change to relay state if within limits
    else:
        print(
            "Error: Could not read temperature. Keeping relay state unchanged."
        )


def main():
    """
    Main function to continuously read temperature and control the relays.
    """
    try:
        while True:
            temperature = read_temperature()
            if temperature is not None:
                print(f"Current Temperature: {temperature:.2f}°C")
                control_relay(temperature)
            else:
                print("Failed to read temperature.")
            time.sleep(5)  # Read temperature every 5 seconds

    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings on exit


if __name__ == "__main__":
    main()

# Filename: heater-contoller.py
# Author: Rebeka B. Mendelsohn
# Created: 2025-05-18
# Description: Controller code that turns on / off a relay based temputure

import RPi.GPIO as GPIO
import Adafruit_DHT  # Use Adafruit_DHT for DHT11
import time  # Import the time module

# Pin definitions
DHT11_PIN = 27  # GPIO pin connected to DHT11 data pin (using the pin from your DHT11.py)
RELAY_PIN = 18  # GPIO pin connected to the relay control pin

# Temperature threshold
TEMP_THRESHOLD = 40  # Temperature in Celsius

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set relay pin as output
GPIO.output(RELAY_PIN, GPIO.LOW)  # Initialize relay to OFF (normally open)

# Initialize DHT11 sensor (no need to create an instance, Adafruit_DHT.read handles it)
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
    Controls the relay based on the given temperature.
    Args:
        temperature (float): The temperature in Celsius.
    """
    if temperature is not None:
        if temperature > TEMP_THRESHOLD:
            print(
                f"Temperature {temperature:.2f}°C is above threshold ({TEMP_THRESHOLD}°C). Turning relay ON."
            )
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn relay OFF
        else:
            print(
                f"Temperature {temperature:.2f}°C is below threshold ({TEMP_THRESHOLD}°C). Turning relay OFF."
            )
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn relay ON
    else:
        print(
            "Error: Could not read temperature.  Keeping relay state unchanged."
        )


def main():
    """
    Main function to continuously read temperature and control the relay.
    """
    try:
        while True:
            temperature = read_temperature()
            if temperature is not None:
                print(f"Temperature: {temperature:.2f}°C")
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

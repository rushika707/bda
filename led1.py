#IR SENSOR WITH BUZZER
import RPi.GPIO as GPIO
import time

sensor = 11
buzzer = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(buzzer, False)

print("Initializing IR Sensor...")
time.sleep(0.5)

print("IR Ready...")
print("")

try:
    while True:
        if GPIO.input(sensor):
            GPIO.output(buzzer, True)
            print("Motion Detected")

            while GPIO.input(sensor):
                time.sleep(0.5)
        else:
            GPIO.output(buzzer, False)

except KeyboardInterrupt:
    GPIO.cleanup()

#DHT11 Temperature and Humidity Sensor
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11
pin = 17

print("Temperature & Humidity")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print(f"Temp:{temperature:0.1f}C | Humidity:{humidity:0.1f}%")
        else:
            print("Failed")

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()

#DHT11 Sensor Reading
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11
pin = 17

print("Temperature & Humidity Sensor Reading")

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print("Temperature:", temperature)
            print("Humidity:", humidity)

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()

#DHT11 with LCD Display
from RPLCD import *
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)

lcd = CharLCD(cols=20, rows=4, pin_rs=35, pin_e=33,
              pins_data=[40,38,36,32], numbering_mode=GPIO.BOARD)

sensor = Adafruit_DHT.DHT11
p = 17

print("Temp & Humidity in progress...")

try:
    while True:
        h, temp = Adafruit_DHT.read_retry(sensor, p)

        print("Humidity:", str(h))
        print("Temperature:", str(temp))

        time.sleep(0.5)

        lcd.cursor_pos = (0,0)
        lcd.write_string(f"Temperature:{temp}")

        lcd.cursor_pos = (1,0)
        lcd.write_string(f"Humidity:{h}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated")
    GPIO.cleanup()

#single led
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

while True:
    print("LED ON")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)

    print("LED OFF")
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
#multiple led's
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setting multiple pins as output
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

while True:
    print("LEDs ON")
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)

    time.sleep(1)

    print("LEDs OFF")
    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

    time.sleep(1)
#single led with switch program
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED as OUTPUT
GPIO.setup(18, GPIO.OUT)

# Switch as INPUT
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(16) == GPIO.HIGH:
        print("Switch ON - LED ON")
        GPIO.output(18, GPIO.HIGH)
    else:
        print("Switch OFF - LED OFF")
        GPIO.output(18, GPIO.LOW)

    time.sleep(0.5)
#buzzer with switch
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

buzzer = 38
switch = 31

gpio.setup(buzzer, gpio.OUT)
gpio.setup(switch, gpio.IN)

def sound_buzzer(event):
    if event == switch:
        gpio.output(buzzer, True)
        print("Buzzer ON")
        time.sleep(1)

        gpio.output(buzzer, False)
        time.sleep(0.5)

gpio.add_event_detect(switch, gpio.RISING,
                      callback=sound_buzzer,
                      bouncetime=1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()
#LED and Buzzer with Switch
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led = 40
switch = 31
buzzer = 19

gpio.setup(led, gpio.OUT, initial=0)
gpio.setup(buzzer, gpio.OUT)
gpio.setup(switch, gpio.IN)

def glow_led_and_sound_buzzer(event):
    if event == switch:
        gpio.output(led, True)
        gpio.output(buzzer, True)

        print("LED & Buzzer ON")
        time.sleep(1.5)

        gpio.output(led, False)
        gpio.output(buzzer, False)

gpio.add_event_detect(switch, gpio.RISING,
                      callback=glow_led_and_sound_buzzer,
                      bouncetime=100)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()
#led with buzzer
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 40
buzzer = 38

GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

while True:
    print("LED & Buzzer ON")
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(buzzer, GPIO.HIGH)

    time.sleep(1)

    print("LED & Buzzer OFF")
    GPIO.output(led, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(1)

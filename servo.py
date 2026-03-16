#Servo Motor Single Cycle (0° → 180°)
import RPi.GPIO as g
import time

g.setmode(g.BOARD)
g.setwarnings(False)

g.setup(11, g.OUT)   # connect servo to pin 11

servo = g.PWM(11, 50)
servo.start(5)

print("wait")
time.sleep(1)

duty = 2

while duty <= 17:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    duty = duty + 2

print("turning back to 0 degrees")

servo.ChangeDutyCycle(2)
time.sleep(0.5)

servo.ChangeDutyCycle(0)
servo.stop()

g.cleanup()
print("cleared")
#Servo Motor Rotation (0° → 180° → 0° Multiple Cycles)
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

servo_pin = 11
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

try:
    cycles = 3
    for i in range(cycles):
        print(f"Cycle {i+1}")

        for angle in range(0, 181, 30):
            print(f"Moving to {angle} degrees")
            set_angle(angle)

        for angle in range(180, -1, -30):
            print(f"Moving to {angle} degrees")
            set_angle(angle)

    print("Completed all cycles")

except KeyboardInterrupt:
    print("Process interrupted")

finally:
    servo.stop()
    GPIO.cleanup()
    print("GPIO cleaned and program exited")
#Servo Motor Angle Control (User Input)
import RPi.GPIO as g
from time import sleep

g.setmode(g.BOARD)
g.setwarnings(False)

control_pin = 11
g.setup(control_pin, g.OUT)

pwm = g.PWM(control_pin, 50)

set_angle = int(input("Enter servo motor rotation angle: "))

pwm.start(0)

delay = 1
duty_cycle = (set_angle / 18) + 2.5

g.output(control_pin, True)
pwm.ChangeDutyCycle(duty_cycle)

sleep(delay)

g.output(control_pin, False)
pwm.ChangeDutyCycle(0)

pwm.stop()
g.cleanup()

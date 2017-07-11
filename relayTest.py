# Test script for 3-ch RPi Relay Board
import RPi.GPIO as GPIO
from time import sleep

# Relay channel definitions
relay1 = 26
relay2 = 20
relay3 = 21
# Initialise GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
# Relays are active-low
GPIO.output(relay1,True)
GPIO.output(relay2,True)
GPIO.output(relay3,True)
sleep(1)

print("Cycling relays")
GPIO.output(relay1,False)
sleep(0.5)
GPIO.output(relay2,False)
sleep(0.5)
GPIO.output(relay3,False)
sleep(1)
print("Done")

GPIO.cleanup()

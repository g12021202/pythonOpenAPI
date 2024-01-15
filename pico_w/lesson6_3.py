# Pins and GPIO
import machine
import time
from machine import Pin
led = Pin("LED", Pin.OUT)
while True:
    print(machine.freq()) # get the current frequency of the CPU
    led.value(1)
    time.sleep(1) # sleep for 1 second
    led.value(0)
    time.sleep(1) # sleep for 1 second
    
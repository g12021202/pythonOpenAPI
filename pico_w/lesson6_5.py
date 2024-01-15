from machine import Pin # Pins and GPIO
import time # Delay and timing

start_ticks = time.ticks_ms() # get millisecond counter
led = Pin("LED", Pin.OUT)
ledStatus = False

while True:
    var_ticks = time.ticks_ms() # get millisecond counter
    if var_ticks - start_ticks == 1000:
        start_ticks = time.ticks_ms() # get millisecond counter
        ledStatus = not ledStatus
        led.value(ledStatus)
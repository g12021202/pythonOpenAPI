from machine import Pin # Pins and GPIO
import time # Delay and timing

start_ticks1 = time.ticks_ms() # get millisecond counter
start_ticks2 = time.ticks_ms() # get millisecond counter
start_ticks3 = time.ticks_ms() # get millisecond counter
led = Pin("LED", Pin.OUT)
ledStatus = False

while True:
    var_ticks = time.ticks_ms() # get millisecond counter
    if time.ticks_diff(time.ticks_ms(), start_ticks1) >= 1000:
        print("過1秒了")
        start_ticks1 = time.ticks_ms() # get millisecond counter
        ledStatus = not ledStatus
        led.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(), start_ticks2) >= 5000:
        print("過5秒了")
        start_ticks2 = time.ticks_ms() # get millisecond counter
        ledStatus = not ledStatus
        led.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(), start_ticks3) >= 10000:
        print("過10秒了")
        start_ticks3 = time.ticks_ms() # get millisecond counter
        ledStatus = not ledStatus
        led.value(ledStatus)
# Blink the onboard LED per second
from machine import Pin, Timer # Pins and GPIO & Timers

led = Pin("LED", Pin.OUT)

def oneSecond(t):
    print("過1秒了")
    # toggle the LED
    led.toggle()
    
tim = Timer(period=1000, mode=Timer.PERIODIC, callback=oneSecond)

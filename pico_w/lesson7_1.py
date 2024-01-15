# Blink the onboard LED (t-1) second and then stop blinking after t seconds
from machine import Pin, Timer # Pins and GPIO & Timers

led = Pin("LED", Pin.OUT)

i = 0

def second1(t):
    global i
    print("過1秒了")
    # toggle the LED
    led.toggle()
    i += 1
    if (i>=3):
        i.deinit()
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
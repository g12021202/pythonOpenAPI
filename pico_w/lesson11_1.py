from machine import Pin
red_led = Pin(15, Pin.OUT)
red_led.value(1)
red_led.value(0)
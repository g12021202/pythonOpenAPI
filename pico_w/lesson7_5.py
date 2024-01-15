from machine import Pin, Timer, ADC

adc = ADC(4)  # create ADC object on ADC pin,最後一個,溫度

led = Pin("LED", Pin.OUT)

def oneSecond(t):
    global i
    print("過1秒了")
    print(adc.read_u16())
    # toggle the LED
    led.toggle()
    
tim = Timer()
tim.init(period=1000, callback=oneSecond)

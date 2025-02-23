from machine import Pin, Timer, ADC
import time

adc = ADC(4)  # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

start_time = 0
duration = 60

def alert():
    global start_time
    if time.ticks_diff(time.ticks_ms(), start_time) >= duration * 1000:
        print("要爆炸了")
        print("傳送訊息")
        start_time = time.ticks_ms()  # get millisecond counter
        

def oneSecond(t):
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - ( reading_v - 0.706 ) / 0.001721
    print(celsius)
    if celsius >= 22:
        alert()

tim = Timer()
tim.init(period=1000, callback=oneSecond)

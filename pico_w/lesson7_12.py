from tools import connect, reconnect
from machine import Pin, Timer, ADC, RTC
import time
import urequests

# https://hook.eu2.make.com/rs3wini1ka7mhjr3qdbd6p9mw73zqhyl?date=2024-1-15-14:25:00&temperature=25.456&from=school
connect()
adc = ADC(4)  # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

start_time = 0
duration = 60

def alert():
    global start_time
    if time.ticks_diff(time.ticks_ms(), start_time) >= duration * 1000:
        rtc = RTC()
        date_tuple = rtc.datetime()
        date_str = f'{date_tuple[0]}-{date_tuple[1]}-{date_tuple[2]}-{date_tuple[4]}:{date_tuple[5]}:{date_tuple[6]}'
        print(date_str)
        print("傳送訊息")
        start_time = time.ticks_ms()
        

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

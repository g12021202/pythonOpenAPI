# Real time clock (RTC)
from machine import RTC

rtc = RTC()
print(rtc.datetime()) # get date and time
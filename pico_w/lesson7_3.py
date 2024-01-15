from machine import ADC, Pin
adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
print(adc.read_u16())         # read value, 0-65535 across voltage range 0.0v - 3.3v

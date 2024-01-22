# from tools import connect, reconnect
import network
from machine import ADC, Timer
import time

# connect()


def hotspotWifi(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print(wlan.isconnected())


adc = ADC(4)  # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

def tenSecondTemperature(t):
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - ( reading_v - 0.706 ) / 0.001721
    timenow = time.localtime()
    print(f"{timenow} 現在溫度是 {celsius}")


# hotspotWifi("wifiName","wifiPassword")
#hotspotWifi("DazhiHotspot","dazhihotspot2005")
hotspotWifi("KUAN-HUNG_iPhone","linkuanhung1202")

tim = Timer()
tim.init(period=10000, callback=tenSecondTemperature)

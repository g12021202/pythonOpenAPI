import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('DazhiHotspot', 'dazhihotspot2005')
print(wlan.isconnected())
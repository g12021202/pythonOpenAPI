from machine import Pin
from tools import connect,reconnect
import time
import urequests

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
#connect()

while True:
    if btn.value():
        #解決按下彈跳
        time.sleep_ms(50)
        if btn.value():
            is_press = True
            red_led.value(1)
    else:
        #解決放開彈跳
        time.sleep_ms(50)
        if btn.value() == False:
            if is_press == True:     
                print('release')
                is_press = False
                '''
                url_str = 'https://自已的網址/pico_w/2024-01-22 16:02:10?address=chicken_KFC&celsius=15.386'
                try:
                    response = urequests.get(url_str)
                    pass
                except:
                    print("ap出現問題")            
                    reconnect()
                else:
                    if response.status_code == 200:            
                        print("傳送訊息成功")
                    else:
                        print("傳送失敗(server出現錯誤)")
                    response.close()
                '''
            
        
            red_led.value(0)
        
    
        
    
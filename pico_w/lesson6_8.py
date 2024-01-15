from machine import Timer # Timers

def fiveSeconds(t):
    print("過5秒了")

def oneSecond(t):
    print("過1秒了")
    
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=fiveSeconds)
tim = Timer(period=1000, mode=Timer.PERIODIC, callback=oneSecond)
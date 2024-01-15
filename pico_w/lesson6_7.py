from machine import Timer # Timers

def fiveSeconds(t):
    print("過5秒了")
    
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=fiveSeconds)

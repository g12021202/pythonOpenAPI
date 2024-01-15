# Delay and timing
import machine
import time
while True:
    print(machine.freq()) # get the current frequency of the CPU
    time.sleep(1) # sleep for 1 second
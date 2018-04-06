import machine
import time


pin16 = machine.Pin(16, machine.Pin.OUT) 
pin2 = machine.Pin(2, machine.Pin.OUT)

while True:
    pin16.value(not pin16.value())
    pin2.value(not pin2.value())
    time.sleep(0.5)



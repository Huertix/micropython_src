# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import time
import network

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.connect('sputnik1', 'Suerte@Munich')
sta_ip = sta_if.ifconfig()[0]
time.sleep_ms(300)
if sta_if.isconnected():
	print("sta_if IP: {} ".format(sta_ip))

#import webrepl
#webrepl.start()
gc.collect()

import pyb
import network
import time
import uping
import machine
import gc
import senko
import netmanager


redLED = pyb.LED(1)
greenLED = pyb.LED(2)
blueLED = pyb.LED(3)

blueLED.on()

def free_mem():
    r = gc.mem_free()
    print('free memory:', r)

def reboot():
    machine.reset()

def clock():
    print('System freq: {:.1f} MHz'.format(machine.freq()[0]/1000000))

blueLED.off()

uping.ping("google.com", count=4, timeout=5000, interval=10, quiet=False, size=64)

clock()

free_mem()

if OTA.fetch():
    print("A newer version is available!")
else:
    print("Up to date!")
    
    
def update():
    if OTA.update():
        print("Updated to the latest version! Rebooting...")
        machine.reset()
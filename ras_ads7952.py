import spidev
import time
import os
from time import sleep

RESTCMD = 0x4000                #0b1000000000000
ManualMode = 0x1080             #0b1000010000000
AutoMode_1 = 0x2c00             #0b1011000000000
AutoMode_2 = 0x3c00             #0b1111000000000

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 500000       #set sampling frequency

resp = spi.xfer([0x40,0x00])    #set manual mode initially
resp = spi.readbytes(2)         #starts read at ch0
resp = spi.readbytes(2)         #restarts read at ch0 everytime
resp = spi.xfer([0x2C,0x00])    #set auto_1 mode
resp = spi.readbytes(2)         #sequential channel read for auto_1 mode

while 1:
    for i in range(0,12):
        resp = spi.readbytes(2)
        print(str(resp)+" : CH "+str(i)+ " -> "+str(resp[1]+resp[0]))
    sleep(0.1)                  #set sampling time in sec
    print("-----------------")

spi.close()
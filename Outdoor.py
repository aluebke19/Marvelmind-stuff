import RoboPiLib as RPL
import setup

from marvelmind import MarvelmindHedge
from time import sleep
import sys

RPL.pinMode(sensor_pin,RPL.INPUT)
def analogRead(pin):
  putPacket(ANREAD, bytearray([5]), 1)
  buff = getPacket()
  return int(buff[3][1]) | (int(buff[3][2]) << 8)

import RPL
RPL.init()
import time
f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

def DT_PWM_Speedrange():
	ServoR = int(raw_input(0))
	RPL.pinMode(ServoR, RPL.PWM)
	ServoL = int(raw_input(1))
	RPL.pinMode(ServoL, RPL.PWM)


hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread

def navigation():
    #Pulls respective values of the hedge for x and y from the position array
    MobileX = float(hedge.position()[1])
    MobileY = float(hedge.position()[2])

    while True:
        MobileX = hedge.position()[1]
        MobileY = hedge.position()[2]
        if RPL.analogRead(1) > 500:  # front left
            RPL.pwmWrite(ServoR, 1250, 3000)
            RPL.pwmWrite(ServoL, 1000, 3000)
            print "1"
        elif RPL.analogRead(2) > 500:  # front right
            RPL.pwmWrite(ServoR, 2000, 3000)
            RPL.pwmWrite(ServoL, 1750, 3000)
            print "2"
        elif RPL.analogRead(3) > 500:   # left side
            RPL.pwmWrite(ServoR, 1550, 3000)
            RPL.pwmWrite(ServoL, 1000, 3000)
            print "3"
        elif RPL.analogRead(4) > 500:   # right side
            RPL.pwmWrite(ServoR, 2000, 3000)
            RPL.pwmWrite(ServoL, 1450, 3000)
            print "4"
        elif 0 > MobileX and 0 > MobileY:
            RPL.pwmWrite(ServoR, 1750, 3000)  # drive straight
            RPL.pwmWrite(ServoL, 1250, 3000)
            print "a"
        elif MobileX < 0 and MobileY > 0:
            RPL.pwmWrite(ServoR, 1550, 3000)  # turn right
            RPL.pwmWrite(ServoL, 1250, 3000)
            print "b"
        elif MobileX > 0 and MobileY < 0:
            RPL.pwmWrite(ServoR, 1750, 3000)   # turn left
            RPL.pwmWrite(ServoR, 1450, 3000)
            print "c"
        elif MobileX == 0 and MobileY == 0:
            RPL.pwmWrite(ServoR, 1500, 3000)         # stop
            RPL.pwmWrite(ServoL, 1500, 3000)
            print "d"
        elif MobileX > 0 and MobileY > 0:
            RPL.pwmWrite(ServoR, 1450, 3000)    # backwards
            RPL.pwmWrite(ServoR, 1550, 3000)
           print "e"
        print MobileX
        print MobileY
        hedge.print_position()


navigation()

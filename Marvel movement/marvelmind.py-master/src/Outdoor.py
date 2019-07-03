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
        if RPL.analogRead(1) > 200:  # front left
            RPL.servoWrite(0, 1450)
            RPL.servoWrite(1, 2000)
            print "1"
        elif RPL.analogRead(2) > 200:  # front right
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(1, 1550)
            print "2"
        elif RPL.analogRead(3) > 200:   # left side
            RPL.servoWrite(0, 1450)
            RPL.servoWrite(1, 2000)
            print "3"
        elif RPL.analogRead(4) > 200:   # right side
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(1, 1550)
            print "4"
        elif 0 > MobileX and 0 > MobileY:
            RPL.servoWrite(0, 1000)  # drive straight
            RPL.servoWrite(1, 2000)
            print "a"
        elif MobileX < 0 and MobileY > 0:
            RPL.servoWrite(0, 1450)  # turn right
            RPL.servoWrite(1, 2000)
            print "b"
        elif MobileX > 0 and MobileY < 0:
            RPL.servoWrite(0, 1000)    # turn left
            RPL.servoWrite(1, 1550)
            print "c"
        elif MobileX == 0 and MobileY == 0:
            RPL.servoWrite(0, 0)         # stop
            RPL.servoWrite(0, 0)
            print "d"
        elif MobileX > 0 and MobileY > 0:
            RPL.servoWrite(0, 1600)    # backwards
            RPL.servoWrite(1, 1400)
           print "e"
        print MobileX
        print MobileY
        hedge.print_position()


navigation()

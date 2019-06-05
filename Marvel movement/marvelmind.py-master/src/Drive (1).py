import setup
from setup import RPL
import RoboPiLib as RPL
sensor_pin = 5
RPL.pinMode(sensor_pin,RPL.INPUT)

from marvelmind import MarvelmindHedge
from time import sleep
import sys

def main():
    hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    while True:
        try:
            sleep(1)
            # print (hedge.position()) # get last position and print
            hedge.print_position()
            if (hedge.distancesUpdated):
				hedge.print_distances()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()

def drive():
    if 1.5 > X and 1.5 > Y:
        RPL.servoWrite(0,1000)  # drive straight
        RPL.servoWrite(1,2000)
    if X < 0 and 2 > Y > 0:
        RPL.servoWrite(0,200)  # turn right
        RPL.servoWrite(1,2000)
    if 2 > X > 0 and Y < 0:
        RPL.servoWrite(0,1000)    # turn left
        RPL.servoWrite(1,200)
    if 2 > X > 1.5 and 2 > Y > 1.5:
        RPL.servoWrite(0,0)         # stop
        RPL.servoWrite(1,0)
    if X > 2 or Y > 2:
        RPL.servoWrite(0,0)    # backwards
        RPL.servoWrite(1,0)

import threading
threading.Thread(target = main, name = 'main').start()
threading.Thread(target = drive, name = 'drive').start()

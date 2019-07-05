from bsmLib import RoboPiLib as RPL
RPL.init()

from marvelmind import MarvelmindHedge
import time
import math
import sys

order = [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11]
t = 1
waycoord = [[Ax, Ay], [Bx, By]]
sensor_pin = 5
RPL.pinMode(sensor_pin,RPL.INPUT)
def analogRead(pin):
  putPacket(ANREAD, bytearray([5]), 1)
  buff = getPacket()
  return int(buff[3][1]) | (int(buff[3][2]) << 8)

hedge = MarvelmindHedge(tty = "/dev/ttyAMC0", adr = None, debug = False)
hedge.start()

def driveMath(intposx, intposy, currentx, currenty, wayx, wayy):
    #gimme fuel gimme fire gimme that which i desire
    dist = math.sqrt((wayx - currentx)**2 + (wayy - currenty)**2)
    u = wayx - intposx
    v = wayy - intposy
    u1 = currentx - intposx
    v1 = currenty - intposy
    return (u*v1 - v*u1)
    #vector maths to see if the turn is up or down

def driveCode(turn):
    if turn > 0:
        RPL.servoWrite(1, 800)
        RPL.servoWrite(0, 1000) #needs to turn right, right motor goes faster
    elif turn < 0:
        RPL.servoWrite(1, 1000)
        RPL.servoWrite(0, 800) #needs to turn left
    else:
        RPL.servoWrite(1, 800)
        RPL.servoWrite(0, 1000)
    time.sleep(0.1)

intposx = float(hedge.position()[1]) #initial coordinates
intposy = float(hedge.position()[2])

RPL.servoWrite(1, 1000)
RPL.servoWrite(0, 1000)
time.sleep(2)
RPL.servoWrite(1, 0)
RPL.servoWrite(0, 0)

def toPoint():
    while True:
        if RPL.analogRead(1) > 200:  # front left
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(1, 1000)
            print "1"
        elif RPL.analogRead(2) > 200:  # front right
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(1, 2000)
            print "2"
        elif RPL.analogRead(3) > 200:   # left side
            RPL.servoWrite(0, 1250)
            RPL.servoWrite(1, 1000)
            print "3"
        elif RPL.analogRead(4) > 200:   # right side
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(1, 1250)
            print "4"

        currentx = float(hedge.position()[1])
        currenty = float(hedge.position()[2])

        turn = driveMath(intposx, intposy, currentx, currenty, wayx, wayy)
        driveCode(turn)
        if dist <= 10:
            RPL.servoWrite(1, 0)
            RPL.servoWrite(0, 0)
            break
        else:
            continue

dord = 1

#this is all pseudocode for my brain, i think
#ideally, this cycles through each element in the list, going to each
#waypoint as it does so. the text files stuff is still messed up.

for dord in order:
    set = int(order[dord]) - 1
    waypoint = waycoord [set]
    wayx = waypoint[0]
    wayy = waypoint[1]
    toPoint()


    #i need to cycle back to the start of the list if it reaches the end

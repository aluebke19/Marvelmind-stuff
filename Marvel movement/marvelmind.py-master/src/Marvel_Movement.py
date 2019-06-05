import RoboPiLib as RPL
import setup
from marvelmind import MarvelmindHedge
from time import sleep
import sys
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread

def navigation():
    #Pulls respective values of the hedge for x and y from the position array
    MobileX = hedge.position()[1]
    MobileY = hedge.position()[2]

    #Values of x and Y for stationary beacon that the robot will go to
    Stationary_Beacon_1_X =# Either we put in a value or get it from thing thing
    Stationary_Beacon_1_Y = # Either we put in a value or get it from thing thing

    #This determines where the robot will need to go based on a positive/negative value
    X = MobileX - Stationary_Beacon_1_X
    Y = MobileY - Stationary_Beacon_1_Y

#These are the four possible combinations. We need to figure out where the robot should go based on these

    if 0 > X and 0 > Y:

    if X > 0 and 0 < Y:

    if X < 0 and Y > 0:

    if X < 0 and Y < 0:

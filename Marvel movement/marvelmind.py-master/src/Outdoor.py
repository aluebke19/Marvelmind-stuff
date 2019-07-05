from bsmLib import RPL
RPL.init()

from marvelmind import MarvelmindHedge
from time import sleep
import sys

sensor_pin = 5
RPL.pinMode(sensor_pin,RPL.INPUT)
def analogRead(pin):
  putPacket(ANREAD, bytearray([5]), 1)
  buff = getPacket()
  return int(buff[3][1]) | (int(buff[3][2]) << 8)

		# 	import RPL
		# 	RPL.init()
		# 	import time
		# 	f_reverse = 1000		ADD IF NECESSARY FOR TALONS
		# 	neutral = 1500
		# 	f_forward = 2000
		#	•anglepersecond = 30

		#def DT_PWM_Speedrange():
			#ServoR = int(raw_input(0))
			#RPL.pinMode(ServoR, RPL.PWM)
			#ServoL = int(raw_input(1))
			#RPL.pinMode(ServoL, RPL.PWM)


hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=None, debug=False) # create MarvelmindHedge thread
hedge.start() # start thread

def navigation():
    #Pulls respective values of the hedge for x and y from the position array
    MobileX = float(hedge.position()[1])
    MobileY = float(hedge.position()[2])

	# analogRead(1) = front  left
	# analogRead(2) = front right
	# analogRead(3) = side left
	# analogRead(4) = side right

    while True:
        MobileX = hedge.position()[1]
        MobileY = hedge.position()[2]
        if RPL.analogRead(1) > 200 or RPL.analogRead(3) > 200:  # front left
            RPL.servoWrite(0, 1450)
            RPL.servoWrite(1, 2000)
            print "1"
        elif RPL.analogRead(2) > 200 or RPL.analogRead(4) > 200:  # front right
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(1, 1550)
            print "2"
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
        elif 1 > MobileX > -1 and 1 > MobileY > -1:
            RPL.servoWrite(0, 0)         # stop
            RPL.servoWrite(0, 0)
            print "d"
        elif MobileX > 1 or MobileY > 1:
            RPL.servoWrite(0, 1600)    # backwards
            RPL.servoWrite(1, 1400)
            print "e"
        print MobileX
        print MobileY
        hedge.print_position()


navigation()

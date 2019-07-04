from bsmLib import RPL
RPL.init()

sensor_pin = 5
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

  # analogRead(1) = side slant left
  # analogRead(2) = side slant right
  # analogRead(3) = front left
  # analogRead(4) = front right
  # analogRead(5) = side left
  # analogRead(6) = side right
  # analogRead(7) = front slant left
  # analogRead(8) = front slant right


while True:
    if RPL.analogRead(7) > 500:         			 # drive in reverse
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 2000)
    if RPL.analogRead(3) < 600 or RPL.analogRead(5) < 600:      # turns right if a wall or object on the left side is detected
        RPL.servoWrite(0, 1450)
        RPL.servoWrite(1, 2000)
    if RPL.analogRead(4) < 600 or RPL.analogRead(6) < 600:      # turns left if a wall or object on the right side is detected
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 1550)
    if 50 > RPL.analogRead(1) - RPL.analogRead(2) > -50:              # drives straight
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
    if RPL.analogRead(2) > RPL.analogRead(1) + 50:                 # turn right if sensor reads the ground
        RPL.servoWrite(0, 1450)
        RPL.servoWrite(1, 2000)
    if RPL.analogRead(1) > RPL.analogRead(2) + 50:                 # turn left if sensor reads the ground
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 1550)
    if RPL.analogRead(3) < 300 and RPL.analogRead(4) < 300:
        break

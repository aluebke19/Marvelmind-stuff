from bsmLib import RoboPiLib as RPL
RPL.init()

RPL.pinMode(sensor_pin,RPL.INPUT)
def analogRead(pin):
  putPacket(ANREAD, bytearray([5]), 1)
  buff = getPacket()
  return int(buff[3][1]) | (int(buff[3][2]) << 8)

#analogRead(1) = back side left
#analogRead(2) = front side left
#analogRead(3) = back side right
#analogRead(4) = front side right
#analogRead(5) = left front
#analogRead(6) = right front
#analogRead(7) = back left front
#analogRead(8) = back right front

def forwards():
    if analogRead (3) < analogRead(1) - 150 and analogRead(4) < analogRead(2) - 150:
        RPL.servoWrite(0, 1750)
        RPL.servoWrite(1, 1250)
    elif RPL.analogRead(2) > RPL.analogRead(1):   # turn right
        RPL.servoWrite(0, 1400)
        RPL.servoWrite(1, 1250)
    elif RPL.analogRead(1) > RPL.analogRead(2): # turn left
        RPL.servoWrite(0, 1250)
        RPL.servoWrite(1, 1400)
    elif 10 > RPL.analogRead(1) - RPL.analogRead(2) > -10 and RPL.analogRead(4) > RPL.analogRead(3):
        RPL.servoWrite(0, 1250)
        RPL.servoWrite(1, 1400)
    elif 10 > RPL.analogRead(1) - RPL.analogRead(2) > -10 and RPL.analogRead(3) > RPL.analogRead(4):
        RPL.servoWrite(0, 1400)
        RPL.servoWrite(1, 1250)
    if RPL.analogRead(5) > 250 and RPL.analogRead(6) > 250 and 25 > RPL.analogRead(5) - RPL.analogRead(6) > -25:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
        backwards()

def backwards():
    if analogRead (1) < analogRead(3) - 150 and analogRead(2) < analogRead(4) - 150:
        RPL.servoWrite(0, 1250)
        RPL.servoWrite(1, 1750)
    elif RPL.analogRead(4) > RPL.analogRead(3):
        RPL.servoWrite(0, 1600)
        RPL.servoWrite(1, 1750)
    elif RPL.analogRead(3) > RPL.analogRead(4):
        RPL.servoWrite(0, 1750)
        RPL.servoWrite(1, 1600)
    elif 10 > RPL.analogRead(1) - RPL.analogRead(2) > 10 and RPL.analogRead(2) > RPL.analogRead(1):   # turn right
        RPL.servoWrite(0, 1750)
        RPL.servoWrite(1, 1600)
    elif 10 > RPL.analogRead(1) - RPL.analogRead(2) > -10 and RPL.analogRead(1) > RPL.analogRead(2): # turn left
        RPL.servoWrite(0, 1600)
        RPL.servoWrite(1, 1750)
    if RPL.analogRead(7) > 250 and RPL.analogRead(8) > 250 and 25 > RPL.analogRead(7) - RPL.analogRead(2) > -25:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
        forwards()

while True:
    forwards()

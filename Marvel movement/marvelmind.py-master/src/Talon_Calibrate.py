import RPL
RPL.init()
import time 

f_reverse = 1000
neutral = 1500
f_forward = 2000

def DT_Servo_Calibration():
  Talon_Number = int(raw_input("Would you like to calibrate one or two talons? Pls print either '1' or '2' > "))
  if Talon_Number == 2:
	ServoR = int(raw_input("Pls input what pin you've inserted your right talon into > "))
	RPL.pinMode(ServoR, RPL.PWM)
	ServoL = int(raw_input("Pls input what pin you've inserted your left talon into > "))
	RPL.pinMode(ServoL, RPL.PWM)
    	print("Now, pls hold down the calibration button, which says 'B/C CAL'.")
    	Finished = str(raw_input("Pls type 'yes', if you are pressing down on the button > "))
    	RPL.pwmWrite(ServoR, 2000, 3000)
    	RPL.pwmWrite(ServoL, 2000, 3000)
    	sleep(2)
    	RPL.pwmWrite(ServoR, 1000, 3000)
    	RPL.pwmWrite(ServoL, 1000, 3000)
    	sleep(2)
    	RPL.pwmWrite(ServoR, 1500, 3000)
    	RPL.pwmWrite(ServoL, 1500, 3000)
    	print("Now, pls release the calibration button. If the talon was successfullu calibrated it should blink green.")
    
  if Talon_Number == 1: 
    	Servo_IVL = int(raw_input("Pls input what pin you've inserted your talon into > "))
	RPL.pinMode(Servo_IVL, RPL.PWM)
    	print("Now, pls hold down the calibration button, which says 'B/C CAL'.")
    	Finished = str(raw_input("Pls type 'yes', if you are pressing down on the button > "))
    	RPL.pwmWrite(Servo_IVL, 2000, 3000)
   	RPL.pwmWrite(Servo_IVL, 1000, 3000)
   	RPL.pwmWrite(Servo_IVL, 1500, 3000)
   	print("Now, pls release the calibration button. If the talon was successfullu calibrated it should blink green.")
    
DT_Servo_Calibration()

import serial
from time import sleep

ser = serial.Serial("/dev/ttyAMA0",9600)
ser.dsrdtr=False
ser.setDTR(level=False)
#wait for conneciton to open
sleep(2)

ser.write("__begin command__")
for i in range(4):
	sleep(0.2)
	ser.write("flick servo")	
	sleep(2)
	ser.write("fetchLightState")
	sleep(0.5)
	data=ser.readline()
	print(data)
ser.write("__end command__")
#wait for final command to end
sleep(1)
ser.close()

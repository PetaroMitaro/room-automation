from speak import speak
import time

h=time.strftime("%H")
m=time.strftime("%M")
if int(h)<12:
	period="am"
else:
	period="pm"
t="it is "+h+":"+m+""+period
speak(t)

import subprocess as sub

def speak(str):
	print "speaking...",str
	sub.call("tts '"+str+"'",shell=True)

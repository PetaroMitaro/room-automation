import subprocess as sub
from speak import speak
from rec import rec
import parseSTT
import processSTT
import re

while True:
	speak("When do you want the alarm for?")
	silent=rec(6)
	if not silent:
		parseSTT.parse()
		file = open("./stt.txt",'r')
		for line in file:
			print line
			if re.search("[0-9]+\shours\s[0-9]+\sminutes",line):
				words=line.split(" ")
				hr=words[0]
				min=words[2]
			print hr,min,period
			speak("alarm will be set for"+line)
			cmd="(crontab -l ; echo "+min+" "+hr+" * * * ~/Room/commands/alarm.sh) | sort - | uniq - | crontab -"
			print cmd
			sub.call(cmd,shell=True)
			quit()
		speak("sorry, I did not hear any valid times. try again")

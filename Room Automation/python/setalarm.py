from crontab import CronTab
import subprocess as sub
from speak import speak
from rec import rec
import parseSTT
import processSTT
import re


cron = CronTab(user='pi')
while True:
	speak("When do you want the alarm for?")
	empty=rec(5)
	if not empty:
		for line in open("stt.txt",'r'):
			time = re.compile("[0-9]+\shours?\s[0-9]+\sminutes?\sp\.?m\.?|a\.?m\.?")	
			if time.search(line):
				print line			
				words = line.split(" ")
				hr = words[0]
				min = words[2]
				period = words[4]
				speak("alarm will be set for "+hr+":"+min+" "+period)
				if re.search("p\.?m\.?",period):
					hr=str(int(hr)+12)
				job=cron.new(command="sudo /home/pi/Room/commands/alarm.sh")
				job.minute.on(min)
				job.hour.on(hr)
				job.enable()
				cron.write()
				quit()
		speak("sorry, I did not hear any valid times. try again")

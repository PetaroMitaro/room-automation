from crontab import CronTab
cron = CronTab(user='pi')
cron.remove_all()
job = cron.new(command="sudo /home/pi/Room/commands/alarm.sh")
job.enable()
cron.write()
print job.is_valid()
for job in cron:
	print job

#!/bin/bash
#read crontab
crontab -l > ~/commands/cron.tmp
if [ -s ~/commands/cron.tmp ];
then
	tts "you have alarms set for"
	while read line
	do
		#each cronjob is a line
		words=( $line )
		#speak first two words in opposite order
		time=$( ~/commands/cvrtTime.sh ${words[1]} ${words[0]} )
		tts "$time"
	done < ~/commands/cron.tmp
	rm ~/commands/cron.tmp
else
	tts "you have no alarms"

fi

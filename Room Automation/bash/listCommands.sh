#!/bin/bash
tts "commands are"
index=0
lines=$( cat ~/commands/processLine.sh | uniq -u)
for line in $lines
do
	len=${#line}
	endPos=$((len-3))
	endPos2=$((len-5))
	startPos=2
	if [[ "$line" == "*\""* ]]
	then
                #first word in command or only word
		if [[ "$line" == *"\"*)" ]]
		then
			command=${line:startPos:endPos2}
			echo $command
			tts "$command"
		else
			command=${line:startPos}
		fi
		commands[$index]=$command
		index=$((index+1))
        elif [[ "$line" ==  *"\"*)" ]]
	then
		#last word in command
		lastIndex=$((index-1))
		command="${commands[lastIndex]} ${line:0:endPos}"
		echo $command
		tts "$command"
		commands[$index]=$command
		index=$((index+1))
	fi
done

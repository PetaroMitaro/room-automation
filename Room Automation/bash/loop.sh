#!/bin/bash

#setup LED indicator
gpio -g mode 17 out
gpio -g mode 18 out
#setup the input
echo "speak at will!"
while true
do
 ~/commands/speech2text.sh 3
  while read key;
  do
    #if keyword is found
   if [[ "$key" == *"Sherlock"* ]];
    then
      tts "Hello Watson, what can I do for you?"
      #listen for 4 seconds for command
      ~/commands/speech2text.sh 4
      cat ~/commands/stt.txt
      while read line;
      do
        #process line an run commands base on this
	echo $line
        ~/commands/processLine.sh "$line"
      done < ~/commands/stt.txt
    fi
  done < ~/commands/stt.txt
done

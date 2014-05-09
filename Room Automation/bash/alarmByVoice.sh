#!/bin/bash

~/commands/speech2text.sh 3
while read line;
do
  echo $line
  set $line
  tts "alarm will be made for"
  cvrtTime=$( ~/commands/cvrtTime.sh $1 $3 )
  tts "$cvrtTime"
  tts "Is that correct?"
  bash ~/commands/speech2text.sh 2
  while read answer;
  do
    if [ "$answer" == "yes" ]
    then
      tts "ok, creating alarm now"
      bash ~/commands/createAlarm.sh "$1" "$3" "*" "*" "*"
      exit
    else
      tts "Oops my bad. try again"
      #go back and ask again?
      bash ~/commands/processLine.sh "set alarm"
    fi
  done < ~/commands/stt.txt
done < ~/commands/stt.txt

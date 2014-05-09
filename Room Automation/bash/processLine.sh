#!/bin/bash

line=$1

case $line in
*"please"*)
  tts "oh how polite of you."
  ;;
esac

case $line in
*"change light"*)
  tts "changing lamp mode"
  minicom -S ~/commands/flick.sh
  ;;
*"follow me"*)
  tts "dont move too quickly! I'm tracking your face"
  sudo python ~/commands/superTrack.py
  ;;
*"list commands"*)
  ~/commands/listCommands.sh
  ;;
*"set alarm"*)
  tts "creating an alarm. Please state the alarm time"
  ~/commands/alarmByVoice.sh
  ;;
*"time"*)
  ~/commands/tellTime.sh
  ;;
*"remove alarm"*)
  tts "removing alarms"
  crontab -r
  ;;
*"nevermind"*)
  tts "ok. whenever you're ready."
  ;;
*"party"*)
  tts "you got it boss. Lets pump the tunes!"
  ~/commands/party.sh
  ;;
*"list alarms"*)
  ~/commands/readAlarms.sh
  ;;
*"stop music"*)
  pkill -SIGSTOP mpg321
  ;;
*"sleep"*)
  tts "good idea. sweet dreams watson"
  ~/commands/goodnight.sh
  ;;
*)
  tts "that literally made no sense. I heard $line"
  ;;
esac

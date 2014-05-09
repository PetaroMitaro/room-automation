if [ $1 -eq 0 ]
then
$1=2
fi
echo "listenining for $1 seconds"
/usr/local/bin/gpio -g write 17 1
arecord -D "plughw:1,0" -d "$1" -q -f cd -t wav | ffmpeg -loglevel panic -y -i - -ar 16000 -acodec flac file.flac  > /dev/null 2>&1
/usr/local/bin/gpio -g write 17 0
wget -q -U "Mozilla/5.0" --post-file file.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v1/recognize?lang=en-us&client=chromium" | cut -d\" -f12  > ~/commands/stt.txt
rm file.flac  > /dev/null 2>&1


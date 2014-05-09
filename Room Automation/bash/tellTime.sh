hr=$(date +%k)
min=$(date +%M)
if [[ $hr > 12 ]]
then
	phr=$((hr-12))
	tts "It is $phr:$min pm"
	echo "It is $phr:$min pm"
else
	tts "It is $hr:$min am"
	echo "It is $hr:$min am"
fi

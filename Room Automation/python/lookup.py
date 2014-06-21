import wikipedia
from speak import speak
import sys

try:
	if len(sys.argv)>1:
		term=sys.argv[1]
		words=term.split(" ")
		term=""
		for i in range(3,len(words)):
			term+=words[i]+" "
	else:
		term=""
	print term
	speak(wikipedia.summary(term,sentences=1))
except:
	speak("sorry. I couldnt find an article on "+term)

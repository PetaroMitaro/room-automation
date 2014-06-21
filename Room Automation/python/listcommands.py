from speak import speak

speak("commands are")
for line in open("./commands/commands.txt","r"):
	speak(line)


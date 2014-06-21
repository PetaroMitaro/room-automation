import subprocess as sub
from rec import rec
import processSTT	
from command import Command

if __name__ == "__main__":
	sub.call("tts 'initiating room automation system'",shell=True)
	Command.initCommands()
	while True:
		empty=rec(6)
		if not empty:
			processSTT.process(open("stt.txt",'r'))

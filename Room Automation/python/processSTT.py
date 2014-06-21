from fuzzywuzzy import fuzz
from command import Command
import time
import re
import subprocess as sub

def keywordDetected():
	file = open('stt.txt','r')
	for line in file:
		if "Sherlock" in line:
			return True
	return False

#returns the best command to be executed
def getCmd(commandList):
	bestCmd=Command("no match found")
	bestCmd.confidence=50
	#go through list of posible spoken commands
	for possibleCmdKey in commandList:
		#rmove the word sherlock
		possibleCmdKey.replace("Sherlock","")
		#compare each to all comand keys
		for cmd in Command.getCommands():
			#get confidence
			cmd.confidence=fuzz.token_set_ratio(possibleCmdKey,cmd.key)
			#check if new closest command
			if (cmd.confidence>bestCmd.confidence):
				bestCmd.key=cmd.key
				bestCmd.confidence=cmd.confidence
				bestCmd.script=cmd.script
				bestCmd.transcript=possibleCmdKey
				if (bestCmd.confidence>90):
					return bestCmd
		
	#return best command to be executed
	return bestCmd

def process(commandList=open("stt.txt",'r')):
	sub.call("gpio -g write 17 1",shell=True)
	sub.call("gpio -g write 18 1",shell=True)
	#make sure key processed command
	if keywordDetected():

		#get the closest command and execute
		bestCmd=getCmd(commandList)
		print bestCmd.script
		bestCmd.execute()

	sub.call("gpio -g write 17 0",shell=True)
	sub.call("gpio -g write 18 0",shell=True)

if __name__ == '__main__':
	Command.initCommands()
	process()

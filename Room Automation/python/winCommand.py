import subprocess as sub
import re

class Command:

	commands = []

	def __init__(self,key):
		self.key=key
		self.confidence=0
		#incase file doesn't exist, create and add print statement
		filename="./commands/"+key.strip().replace(" ","")+".py"
		#file = open(filename,'a')		
		
		#set python code to be executed
		self.script="sudo python "+filename

	def execute(self):
		print "executing:",self.script
		#sub.call(self.script,shell=True)


	@staticmethod
	def getCommands():
		cmds = [Command("hello"),Command("time"),Command("set alarm"),Command("jump"),Command("bye")]
		return cmds

	#@staticmethod
	#def initCommands():
		#file = open("./commands/commands.txt",'r')
		#for line in file:
		#	Command.commands.append(Command(line))

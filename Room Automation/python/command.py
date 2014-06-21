import subprocess as sub
import re

class Command:

	commands = []

	def __init__(self,key):
		self.key=key
		self.confidence=0
		self.transcript=""
		#incase file doesn't exist, create and add print statement
		self.filename="./commands/"+key.strip().replace(" ","")+".py"
		file = open(self.filename,'a')		
		
		#set python code to be executed
		self.script="sudo python "+self.filename

	def execute(self):
		self.script=self.script+" '"+self.transcript+"'"
		print "executing:",self.script
		sub.call(self.script,shell=True)

	@staticmethod
	def getCommands():
		return Command.commands

	@staticmethod
	def initCommands():
		file = open("./commands/commands.txt",'r')
		for line in file:
			Command.commands.append(Command(line))

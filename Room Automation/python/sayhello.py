from speak import speak
import random

compliments=["damn sexy","drop dead gorgous","stunning","absolutely incredible","freaking adorkable","amazing","beautiful"]
file = open("/home/pi/Room/stt.txt",'r')
line=file.readline()
words=line.split(" ")
name=words[len(words)-1]
if "my" in words:
	name="babe"
speak("hello "+name+"... dont you look "+random.choice(compliments)+" today")

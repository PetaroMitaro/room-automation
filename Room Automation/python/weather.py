import re
from speak import speak
from feedparser import parse

feed = parse("http://weather.yahooapis.com/forecastrss?w=2506736")
weather = feed['entries'][0]['summary_detail']['value']
lines = weather.split('\n')
report = lines[2][:-6]
report=re.sub(' F',' Fahrenheit',report)
speak("the current weather is. "+report)
for i in range(4,len(lines)-2):
	report = lines[i][:-6]
	report=re.sub('Sun ','Sunday ',report)
	report=re.sub('Mon ','Monday ',report)
	report=re.sub('Tue ','Tuesday ',report)
	report=re.sub('Wed ','Wednesday ',report)
	report=re.sub('Thu ','Thursday ',report)
	report=re.sub('Fri ','Friday ',report)
	report=re.sub('Sat ','Saturday ',report)
	speak(report)

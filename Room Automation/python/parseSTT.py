import subprocess as sub
import json
import httplib

def post():
	with open("stt.flac", "r+") as f:
		audio=f.read()
	url = "www.google.com"
	path = "/speech-api/v2/recognize?lang=en-us&key=AIzaSyAzliO_woZ24h2dbJjLYYv9msUM7-ls_ns"
	headers = { "Content-type": "audio/x-flac; rate=16000" };
	conn = httplib.HTTPSConnection(url)
	conn.request("POST", path, audio, headers)
	response = conn.getresponse()
	data = response.read()
	split=data.split("\n")
	return json.loads(split[len(split)-2])

def parse():
	empty=True
	sub.call("gpio -g write 18 1",shell=True)
	f = open('stt.txt','w')
	sub.call("avconv -i stt.wav  -y stt.flac -loglevel quiet",shell=True)
	#sub.call("avconv -i stt.wav  -y stt.flac",shell=True)
	data=post()
	f.truncate()
	if len(data['result'])>0:
		alt = data['result'][0]['alternative']
		for item in alt:
			trans=item['transcript']
			f.write(trans)
			empty=False
			f.write("\n")
	sub.call("gpio -g write 18 0", shell=True)
	return empty
if __name__ == '__main__':
	parse()

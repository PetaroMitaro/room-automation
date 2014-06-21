import sys
from sys import byteorder
from array import array
from struct import pack
import time
import os
import pyaudio
import wave
import parseSTT
import processSTT

THREASHOLD = 3000
LOUD_COUNT=0
LOUD_COUNT_THREASHOLD=7
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000

def record(duration):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')
    silent=True
    start = time.time()   
    LOUD_COUNT=0
    os.system("gpio -g write 17 1")
    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)
        num_silent += 1
	if max(snd_data)>THREASHOLD:
	    print 'not silent',max(snd_data)
	    LOUD_COUNT=LOUD_COUNT+1
	    if (LOUD_COUNT>LOUD_COUNT_THREASHOLD):
		    silent = False
        if (time.time()-start>=duration):
	    os.system("gpio -g write 17 0")
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    return silent, sample_width, r

def rec(duration):
    silent, sample_width, data = record(duration)
    data = pack('<' + ('h'*len(data)), *data)
    wf = wave.open('stt.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
    if not silent:
	return parseSTT.parse()
    else:
	return True

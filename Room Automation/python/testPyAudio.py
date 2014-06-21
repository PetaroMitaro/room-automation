import pyaudio

# audio setup
CHUNK = 8192    # input buffer size in frames
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
# open sound card data stream
npoints = 1000000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)
try:
    print "RATE %d" % RATE,
    x = stream.read(npoints)
    print "OK"
except IOError:
    print "FAIL"
stream.stop_stream()
stream.close()
p.terminate()

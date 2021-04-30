import requests
import os
import datetime
import pyaudio
import win32api
import wave

class samples:
    def __init__(self, name):
        self.name = name

    def add_sample(self, name):
        path = '/' + name
        today = datetime.today()
        now = datetime.now()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5
        filename = '' + name + '' + today + ' ' + now + '.wav'
        if(os.path.isdir(name) == True):
            py = pyaudio.PyAudio()

            stream = py.open(format=FORMAT,
                            channels=CHANNELS,
                            rate = RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            win32api.MessageBox(0, 'Recording', 'Voice Sample')

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            win32api.MessageBox(0, 'Recording Finished', 'Voice Sample')

            stream.stop_stream()
            stream.close()
            py.terminate()

            wf = wave.open(filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(py.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close( )




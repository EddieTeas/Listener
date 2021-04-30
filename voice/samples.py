import requests
import os
from datetime import date, datetime
import pyaudio
import win32api
import wave

class samples:
    def __init__(self, name):
        self.name = name
        yo = self.cpath(name)
        bro = self.record(name)




    def cpath(self, name):
        path = '/Users/edtea/OneDrive/Documents/GitHub/Listener/User_samps'
        # win32api.MessageBox(0, 'Recording ' + name, 'Voice Sample')

        if os.path.isdir(path+ '/' + name) != True:  # if this directory doesn't exist

                os.mkdir(path + '/' + name)  # make it
                os.chdir(path + '/' + name) #go into the correct directory

        else:
            os.chdir(path + '/'+ name)#go into the correct directory

    def add_sample(self, name):

        blah = self.cpath(name) #checks which dir we are in and changes it
        yah = self.record(name) #calls the voice methods

        

    def record(self, name): #records the voice smaples
        today = date.today()
        now = datetime.now()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 5

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%b %d %Y - %H %M")  #08 34 - Nov 18 2018

        filename = ' ' + name + ' ' + timestampStr + '.wav'

        print(filename)

        py = pyaudio.PyAudio()

        stream = py.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         frames_per_buffer=CHUNK)

        win32api.MessageBox(0, 'Recoding starts when you click the button', 'Voice Sample')

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
        wf.close()


if __name__ == "__main__":
    name = samples('Ed')

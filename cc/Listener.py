import requests
import speech_recognition as sr
from tkinter import *
from datetime import date

class Listener:
    def __init__(self, token):
        self.rec = None
        self.mic = None
        self.api_token = token
        self.seq = 0
        self.post_params = {'seq': str(self.seq), 'lang': 'en-US'}
        self.payload = ""
        self.mic_timeout = 60000
        self.phrase_time_limit = 10
        self.init_seq()

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, traceback):
        print('Exit.')

    def init_seq(self):
        self.seq = 0

    def post_transcript(self, transcript):
        self.post_params['seq'] = str(self.seq)
        request = requests.post(self.api_token,
                                params=self.post_params, data=transcript.encode('utf-8'),
                                headers={'Content-type': 'text/plain; charset=utf-8'})
        print(request.text)
        self.seq += 1

    def run(self):
        today = date.today()
        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        today = str(today) #turns date into a string
        user ="user E" #wanted to have the user made
        while True:
            try:
                with self.mic as source:
                    self.rec.adjust_for_ambient_noise(source)
                    try:
                        f = open("transcript " + today + ".txt", "a") #opens transcript for the day
                        audio = self.rec.listen(source, timeout=self.mic_timeout,
                                                phrase_time_limit=self.phrase_time_limit)
                        self.payload = self.rec.recognize_google(audio, language=self.post_params['lang'])
                        print(self.payload)
                        f.write(user + ": " + str(self.payload))
                        f.write("\n \n")
                        f.close()
                    except KeyboardInterrupt:
                        break
                    except sr.WaitTimeoutError:
                        print("Listening Timed Out.")
                        continue
                    except sr.UnknownValueError:
                        print("Speech Undetected.")
                        continue
                    except:
                        print('Unknown Error.')
                        raise

                self.post_transcript(self.payload)
            except KeyboardInterrupt:
                break



"""
if __name__ == "__main__":
    cc = Listener()
    with cc:
        cc.run()
"""
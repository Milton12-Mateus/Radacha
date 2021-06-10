"""
#Nosso Ficheiro Main(Principal)

import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source) # Define Microfone como Fonte de áudio
        print(r.recognize_google(audio, language='pt')) """
        
        
from vosk import Model, kaldiRecognizer
import os

if not os.path.exists("model"):
	print("Please download the model from https://https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
	exit (1)

import pyaudio

model = Model(model)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.Pyaudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
	data = stream.read(4000)
	if len(data) == 0:
		break
	if rec.AcceptWaveform(data):
		print(rec.Result())
	else:
		print(rec.PartialResult())

print(rec.FinalResult())
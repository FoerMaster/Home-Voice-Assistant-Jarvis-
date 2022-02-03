#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vosk import Model, KaldiRecognizer
import os, json
import recognizer as recon
import music
import library_speech as ls
import winsound
import urllib.request, json
import urllib.parse
import rpshare

rpshare.init()

import plugins.hello

print(plugins.hello.answers)

music.login()

if not os.path.exists("model"):
    print(
        "Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit(1)

import pyaudio

model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
winsound.Beep(2500, 500)

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        x = json.loads(rec.Result())
        if len(x["text"]) > 0:
            print("Услышал: "+x["text"])
            if ls.waitforanswer != None:
                ls.waitforanswer(x["text"])
                ls.waitforanswer = None
            else:
                recon.recognize_callback(x["text"])

        #

    else:
        # print(rec.PartialResult())
        pass

print(rec.FinalResult())
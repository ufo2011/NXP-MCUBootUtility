#!/usr/bin/env python

import sys
import os
import wave
import pyaudio

def playSoundEffect( exeTopRoot, isQuiet, soundFilename ):
    if isQuiet:
        return
    wavPath = os.path.join(exeTopRoot, 'sound', 'mario', soundFilename)
    if os.path.isfile(wavPath):
        wavFile =  wave.open(wavPath, "rb")
        wavPyaudio = pyaudio.PyAudio()
        wavStream = wavPyaudio.open(format=wavPyaudio.get_format_from_width(wavFile.getsampwidth()),
                                    channels=wavFile.getnchannels(),
                                    rate=wavFile.getframerate(),
                                    output=True)
        wavData = wavFile.readframes(1024)
        while wavData != '':
            wavStream.write(wavData)
            wavData = wavFile.readframes(1024)
        wavStream.stop_stream()
        wavStream.close()
        wavPyaudio.terminate()



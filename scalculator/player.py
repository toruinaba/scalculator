import pyaudio
import numpy as np


def play_wave(stream, samples):
    stream.write(samples.astype(np.float32).tobytes())

def player(notes):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=44100,
        frames_per_buffer=1024,
        output=True)
    print("play")
    for note in notes:
        play_wave(stream, note)
    stream.close()

from enum import IntEnum
import numpy as np


RATE = 44100


class Note_name(IntEnum):
    C = 0
    Cs = 1
    D = 2
    Ef = 3
    E = 4
    F = 5
    Fs = 6
    G = 7
    Af = 8
    A = 9
    Bf = 10
    B = 11

    def __add__(self, other):
        if isinstance(other, Interval):
            return Note_name((int(self) + int(other)) % 12)
        elif isinstance(other, int):
            return Note_name((int(self) + other) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Note_name((int(self) - int(other)) % 12)
        elif isinstance(other, Note_name):
            return Interval((int(self) - int(other)) % 12)
        elif isinstance(other, int):
            return Note_name((int(self) - int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")


class Interval(IntEnum):
    _R = 0
    _f9th = 1
    _9th = 2
    _m3th = 3
    _M3th = 4
    _4th = 5
    _a4th = 6
    _P5th = 7
    _f13th = 8
    _13th = 9
    _m7th = 10
    _M7th = 11

    def __add__(self, other):
        if isinstance(other, Interval) or isinstance(other, int):
            return Interval((int(self) + int(other)) % 12)
        elif isinstance(other, Note):
            return Note_name((int(self) + int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")
    
    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval((int(self) - int(other)) % 12)
        elif isinstance(other, Note_name):
            return Note_name((int(self) - int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")     


class Tone:
    A = 440

    def __init__(self, note: Note_name, octave: int):
        self.note_name = note
        self.octave = octave
    
    @property
    def frequency(self):
        int_name = int(self.note_name)
        tone_num = int_name + 12 * self.octave
        return Tone.A * 2 ** ((tone_num - 69) / 12)


class Rythm:
    def __init__(self, bpm: int, beat_n: int, beat_d: int):
        self.bpm = bpm
        self.beat_n = beat_n
        self.beat_d = beat_d


class Note:
    RATE = 44100

    def __init__(self, tone: Tone, rythm: Rythm):
        self.tone = tone
        self.rythm = rythm
        self.l = (60 / self.rythm.bpm) * self.rythm.beat_n / self.rythm.beat_d * 4
    
    def wave(self, gain):
        slen = int(self.l * Note.RATE)
        t = self.tone.frequency * np.pi * 2 / RATE
        print(self.tone.frequency)
        return np.sin(np.arange(slen) * t) * gain


class Notes_base:
    intervals = ()

    def __init__(self, note: Note_name):
        self.key = note

    def from_str(cls):
        pass

    @property
    def note(self):
        return [self.key + x for x in self.intervals]
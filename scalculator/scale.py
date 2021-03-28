from abc import ABC, abstractclassmethod
from .material import Interval, Note

class Scale_base:
    intervals = ()

    def __init__(self, note: Note):
        self.key = note

    def from_str(cls):
        pass

    @property
    def note(self):
        return [self.key + x for x in self.intervals]


class Diatonic_major_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._M7th
    )

    def __init__(self, note: Note):
        super().__init__(note)


class Natural_minor_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note):
        super().__init__(note)


class Harmonic_minor_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._M7th
    )

    def __init__(self, note: Note):
        super().__init__(note)


class Ionian_scale(Diatonic_major_scale):
    def __init__(self, note: Note):
        super().__init__(note)
    

class Dorian_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._m7th
    )

    def __init__(self, note: Note):
        super().__init__(note)
    

class Phrygian_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._f9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note):
        super().__init__(note)


class Lydian_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._a4th,
        Interval._P5th,
        Interval._13th,
        Interval._M7th
    )

    def __init__(self, note: Note):
        super().__init__(note)


class Mixolydian_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._m7th
    )

    def __init__(self, note: Note):
        super().__init__(note)
    

class Aeolian_scale(Natural_minor_scale):
    def __init__(self):
        super().__init__(note)


class Locrian_scale(Scale_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._a4th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note):
        super().__init__(note)
    
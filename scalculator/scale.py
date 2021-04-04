from abc import ABC, abstractclassmethod
from .material import Interval, Note_name, Notes_base


class Diatonic_major(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._M7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)


class Natural_minor(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)


class Harmonic_minor(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._M7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)


class Ionian(Diatonic_major):
    def __init__(self, note: Note_name):
        super().__init__(Note_name)
    

class Dorian(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._m7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)
    

class Phrygian(Notes_base):
    intervals = (
        Interval._R,
        Interval._f9th,
        Interval._m3th,
        Interval._4th,
        Interval._P5th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)


class Lydian(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._a4th,
        Interval._P5th,
        Interval._13th,
        Interval._M7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)


class Mixolydian(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._M3th,
        Interval._4th,
        Interval._P5th,
        Interval._13th,
        Interval._m7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)
    

class Aeolian(Natural_minor):
    def __init__(self, note: Note_name):
        super().__init__(note)


class Locrian(Notes_base):
    intervals = (
        Interval._R,
        Interval._9th,
        Interval._m3th,
        Interval._4th,
        Interval._a4th,
        Interval._f13th,
        Interval._m7th
    )

    def __init__(self, note: Note_name):
        super().__init__(note)
    
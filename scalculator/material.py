from enum import IntEnum


class Note(IntEnum):
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
            return Note((int(self) + int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Note((int(self) - int(other)) % 12)
        elif isinstance(other, Note):
            return Interval((int(self) - int(other)) % 12)
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
        if isinstance(other, Interval):
            return Interval((int(self) + int(other)) % 12)
        elif isinstance(other, Note):
            return Note((int(self) + int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")
    
    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval((int(self) - int(other)) % 12)
        elif isinstance(other, Note):
            return Note((int(self) - int(other)) % 12)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Interval' and '{type(other)}'")     


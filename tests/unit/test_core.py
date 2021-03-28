from scalculator.material import Note, Interval

class Test_note:
    def test_note_add1(self):
        expected = Note.Cs
        assert expected == Note.C + Interval._f9th
    
    def test_note_sub1(self):
        expected = Note.D
        assert expected == Note.C - Interval._m7th
    
    def test_note_sub2(self):
        expected = Interval._m7th
        assert expected == Note.C - Note.D

class Test_interval:
    def test_interval_add1(self):
        expected = Interval._9th
        assert expected == Interval._R + Interval._9th
    
    def test_interval_sub1(self):
        expected = Interval._4th
        assert expected == Interval._R - Interval._P5th

from scalculator.material import Note_name, Interval

class Test_note:
    def test_note_add1(self):
        expected = Note_name.Cs
        assert expected == Note_name.C + Interval._f9th
    
    def test_note_sub1(self):
        expected = Note_name.D
        assert expected == Note_name.C - Interval._m7th
    
    def test_note_sub2(self):
        expected = Interval._m7th
        assert expected == Note_name.C - Note_name.D

class Test_interval:
    def test_interval_add1(self):
        expected = Interval._9th
        assert expected == Interval._R + Interval._9th
    
    def test_interval_sub1(self):
        expected = Interval._4th
        assert expected == Interval._R - Interval._P5th

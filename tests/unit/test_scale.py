import scalculator.scale as scale
from scalculator.material import Note_name, Interval

class Test_scale:
    def test_diatonic_major(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Diatonic_major(key).note
        expected = [Note_name.C, Note_name.D, Note_name.E, Note_name.F, Note_name.G, Note_name.A, Note_name.B]
        # assert
        assert expected == actual

    def test_natural_minor(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Natural_minor(key).note
        expected = [Note_name.C, Note_name.D, Note_name.Ef, Note_name.F, Note_name.G, Note_name.Af, Note_name.Bf]
        # assert
        assert expected == actual

    def test_harmonic_minor(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Harmonic_minor(key).note
        expected = [Note_name.C, Note_name.D, Note_name.Ef, Note_name.F, Note_name.G, Note_name.Af, Note_name.B]
        # assert
        assert expected == actual

    def test_dorian(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Dorian(key).note
        expected = [Note_name.C, Note_name.D, Note_name.Ef, Note_name.F, Note_name.G, Note_name.A, Note_name.Bf]
        # assert
        assert expected == actual

    def test_phrygian(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Phrygian(key).note
        expected = [Note_name.C, Note_name.Cs, Note_name.Ef, Note_name.F, Note_name.G, Note_name.Af, Note_name.Bf]
        # assert
        assert expected == actual

    def test_lydian(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Lydian(key).note
        expected = [Note_name.C, Note_name.D, Note_name.E, Note_name.Fs, Note_name.G, Note_name.A, Note_name.B]
        # assert
        assert expected == actual

    def test_mixolydian(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Mixolydian(key).note
        expected = [Note_name.C, Note_name.D, Note_name.E, Note_name.F, Note_name.G, Note_name.A, Note_name.Bf]
        # assert
        assert expected == actual

    def test_locrian(self):
        # arrange
        key = Note_name.C
        # act
        actual = scale.Locrian(key).note
        expected = [Note_name.C, Note_name.D, Note_name.Ef, Note_name.F, Note_name.Fs, Note_name.Af, Note_name.Bf]
        # assert
        assert expected == actual
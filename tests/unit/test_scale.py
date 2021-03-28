import scalculator.scale as scale
from scalculator.material import Note, Interval

class Test_diatonic_major_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Diatonic_major_scale(key).note
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.B]
        # assert
        assert expected == actual


class Test_natural_minor_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Natural_minor_scale(key).note
        expected = [Note.C, Note.D, Note.Ef, Note.F, Note.G, Note.Af, Note.Bf]
        # assert
        assert expected == actual


class Test_harmonic_minor_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Harmonic_minor_scale(key).note
        expected = [Note.C, Note.D, Note.Ef, Note.F, Note.G, Note.Af, Note.B]
        # assert
        assert expected == actual


class Test_Dorian_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Dorian_scale(key).note
        expected = [Note.C, Note.D, Note.Ef, Note.F, Note.G, Note.A, Note.Bf]
        # assert
        assert expected == actual


class Test_Phrygian_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Phrygian_scale(key).note
        expected = [Note.C, Note.Cs, Note.Ef, Note.F, Note.G, Note.Af, Note.Bf]
        # assert
        assert expected == actual


class Test_Lydian_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Lydian_scale(key).note
        expected = [Note.C, Note.D, Note.E, Note.Fs, Note.G, Note.A, Note.B]
        # assert
        assert expected == actual


class Test_Mixolydian_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Mixolydian_scale(key).note
        expected = [Note.C, Note.D, Note.E, Note.F, Note.G, Note.A, Note.Bf]
        # assert
        assert expected == actual


class Test_Locrian_scale:
    def test_scale(self):
        # arrange
        key = Note.C
        # act
        actual = scale.Locrian_scale(key).note
        expected = [Note.C, Note.D, Note.Ef, Note.F, Note.Fs, Note.Af, Note.Bf]
        # assert
        assert expected == actual
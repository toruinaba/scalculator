from scalculator import player, scale, material

def test_player():
    # arange
    key = material.Note_name.A
    ns = scale.Diatonic_major(key)
    rythm = material.Rythm(120, 1, 4)
    base_oct = 5
    tones = [material.Tone(x, base_oct) if int(key) <= int(x) else material.Tone(x, base_oct + 1) for x in ns.note]
    notes = [material.Note(x, rythm).wave(0.2) for x in tones]
    # act
    player.player(notes)

if __name__ == "__main__":
    test_player()
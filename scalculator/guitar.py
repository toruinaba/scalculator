from scalculator.material import Note_name

class Guitar:
    flet_number = 24
    string_number = 6

    def __init__(self):
        tunings = [
            Note_name.E, Note_name.B, Note_name.G,
            Note_name.D, Note_name.A, Note_name.E
        ]
        octaves = [6, 5, 5, 5, 4, 4]
        self.keys, self.flets, self.strings = self.graph_struct(tunings, octaves)
    
    def graph_struct(self, tunings, octaves):
        keys = {}
        flets = {}
        strings = {}
        for key in Note_name:
            keys[key] = {"flet": [], "string": []}
        for flet in range(Guitar.flet_number):
            flets[flet] = {"key": []}
            for string in range(1, Guitar.string_number + 1):
                tmp_key = tunings[string - 1] + flet
                flets[flet]["key"].append(tmp_key)
                keys[tmp_key]["flet"].append(flet)
                keys[tmp_key]["string"].append(string)
                strings[string] = {"key": [tunings[string - 1] + x for x in range(Guitar.flet_number)]}
        return keys, flets, strings
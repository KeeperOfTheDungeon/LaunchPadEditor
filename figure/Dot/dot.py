from Figure.Figure import Figure


class Dot(Figure):

    _name = "Dot"

    def __init__(self, root, midi_out):
        super().__init__(Dot._name ,root, midi_out)
        pass


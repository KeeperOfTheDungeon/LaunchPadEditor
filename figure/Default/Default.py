from Figure.Figure import Figure


class Default(Figure):

    _name = "Default"

    def __init__(self, root, midi_out):
        super().__init__(Default._name,root, midi_out)
        pass
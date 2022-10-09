from figure.figure import Figure


class Line(Figure):
      def __init__(self, root, midi_out):
        self._clock_divider = 20
        self._root = root
        self._midi_out = midi_out
        self._phase = True
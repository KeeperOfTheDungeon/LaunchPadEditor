from Figure.Figure import Figure


class Blink(Figure):

    _name = "Blink"

    def __init__(self, root, midi_out):
        self._clock_divider = 20
        self._root = root
        self._midi_out = midi_out
        self._phase = True

    def midi_clock(self):
        self._clock_divider += 1
        if self._clock_divider > 20:
            self._phase = not self._phase
            if (self._phase):
                self._midi_out.note_on(self._root, velocity=100, channel=0)
            else:
                self._midi_out.note_on(self._root, velocity=50, channel=0)


    def get_root(self):
        return self._root


    def modulate(self):
        # modulate color
        # modulate brightness
        pass    

    
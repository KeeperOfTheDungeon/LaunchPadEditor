class Figure:
    def __init__(self, name, root, midi_out):
        self._name = name
        self._root = root
        self._midi_out = midi_out
        self._is_active = False

        self._running = False
        

    def get_name(self):
        return self._name


    def reset(self):
        pass

    def midi_clock(self):
        pass

    def system_clock(self):
        pass


    def modulate(self):
        pass

   
    def get_editor(self):
        pass

class Pad:
    def __init__(self, index):
        self._index = index
        self._note = index


    def get_note(self):
        return self._note


    def sent_note(self, note):
        self._note = note 


    def set_figure(self, figure):
        self._figure = figure


    def get_figure(self):
        return self._figure 
from launchpad.pad import Pad


class PadList:
    def __init__(self):
          self._pads = [Pad(x) for x in range(0,109)]


    def set_figure( self, pad, figure):
        self._pads[pad].set_figure(figure)

    def get_figure(self, pad):
        return self._pads[pad].get_figure()

    def size(self):
        return (len(self._pads))
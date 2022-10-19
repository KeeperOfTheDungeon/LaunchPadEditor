
class Frame:

    def __init__(self, x_size, y_size):
        self.set_size(x_size, y_size)
       

    def set_size(self, x_size, y_size):
        self._x_size = x_size
        self._y_size = y_size
        self._matrix = 2

    def set_pixel(self, x_pos, y_pos, color):
        if x_pos < self._x_size and y_pos < self._y_size:
            pass

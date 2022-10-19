
class Color:
    def __init__(self):
        self._red = 0
        self._green = 0
        self._blue = 0
        self._alpha = 0


    def set_color(self, color):
        self._red = color._red
        self._green = color._green
        self._blue = color._blue
        self._alpha = color._alpha

    def set_rgba(self, red, green, blue, alpha):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha




    def get_red(self):
        return self._red

    def set_red(self, red):
        self._red = red

    def get_green(self):
        return self._green

    def set_green(self, green):
        self._green = green    

    def get_blue(self):
        return self._blue

    def set_blue(self, blue):
        self._blue = blue        

    def to_(self):
        message = [self._red, self._green, self._blue]    
        return(message)

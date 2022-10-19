
from Color.Color import Color


DISPLAY_WIDTH = 10
DISPLAY_HEIGHT = 11 

class Display:
    def __init__(self):
        self._dirty_matrix = [[False for x in range(DISPLAY_WIDTH)] for y in range(DISPLAY_HEIGHT)] 
        self._color_matrix = [[Color() for x in range(DISPLAY_WIDTH)] for y in range(DISPLAY_HEIGHT)] 



    def set_pxel(self, x_pos, y_pos, color):
        if x_pos < DISPLAY_WIDTH and y_pos <DISPLAY_HEIGHT:
            self._color_matrix[y_pos] [x_pos].set_color(color)
            self._dirty_matrix[y_pos] [x_pos] = True

    def get_(self):
        message = []  
        for x_index in range(DISPLAY_WIDTH):
            for y_index in range(DISPLAY_HEIGHT):
                if self._dirty_matrix[y_index] [x_index] == True:
                    position = y_index * DISPLAY_WIDTH + x_index
                    message = message + [3, position] + self._color_matrix[y_index] [x_index].to_()
                    self._dirty_matrix[y_index] [x_index] = False
        
        return message
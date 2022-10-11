from tkinter import Label
from Figure.FigureEditor import FigureEditor


class BlinkEditor(FigureEditor):
    def __init__(self):
        pass


    def create(self, root):
        super().create(root)
        w = Label(self._frame , text="Blink")
        w.place(x=10, y = 10, width = 40, height= 20)
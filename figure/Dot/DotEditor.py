from tkinter import Label
from figure.FigureEditor import FigureEditor


class DotEditor(FigureEditor):
    def __init__(self):
        pass


    def create(self, root):
        super().create(root)
        w = Label(self._frame , text="dot")
        w.place(x=10, y = 10, width = 40, height= 20)
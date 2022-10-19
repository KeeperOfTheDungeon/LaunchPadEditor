from tkinter import Label
from Figure.Disc.Disc import Disc
from Figure.FigureEditor import FigureEditor


class DiscEditor(FigureEditor):
    def __init__(self):
        pass



    def create(self, root):
        super().create(root)
        w = Label(self._frame , text="disc")
        w.place(x=10, y = 10, width = 40, height= 20)


    def init_figure(self):
        self._figure = Disc("",None)
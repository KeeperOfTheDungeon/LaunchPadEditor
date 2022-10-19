from tkinter import Label
from tkinter.colorchooser import askcolor
from Figure.Dot.Dot import Dot
from Figure.FigureEditor import FigureEditor


class DotEditor(FigureEditor):
    def __init__(self):
        pass


    def create(self, root):
        super().create(root)
        w = Label(self._frame , text="dot")
        w.place(x=10, y = 10, width = 40, height= 20)

        #colors = askcolor(title="Tkinter Color Chooser")
        pass

    def init_figure(self):
        self._figure = Dot()

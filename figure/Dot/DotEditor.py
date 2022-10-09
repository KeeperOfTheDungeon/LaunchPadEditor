from tkinter import Label
from figure.FigureEditor import FigureEditor


class DotEditor(FigureEditor):
    def __init__(self, frame):
        super().__init__(frame)
        w = Label(frame , text="dot")
        w.place(x=10, y = 40, width = 40, height= 20)
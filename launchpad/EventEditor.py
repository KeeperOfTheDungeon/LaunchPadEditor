from tkinter import Frame, Label
from tkinter.ttk import Combobox
from figure.Dot.DotEditor import DotEditor

from figure.FigureEditor import FigureEditor


class EventEditor:
    def __init__(self,  x_pos, y_pos, figures):
        self._frame = Frame( bg = "GRAY", borderwidth=1)  
        
        self._frame.config(highlightbackground = "RED", highlightcolor= "RED") 
        self._frame.place(height=400, width = 200, x=x_pos, y=y_pos)
        
        self._frame.bind("<ButtonRelease-1>", self.mouse_released)


        self.make(figures)

        self._frame.update()


    def mouse_released(self, event):
        print("Mouse released")


    def make(self, figures):
        w = Label(self._frame , text="Figure")
        w.place(x=10, y = 20, width = 60, height= 20)
		#w.pack()

        liste = list(figures.keys())

        self._combo_figure = Combobox(self._frame, values = liste)

        """self._combo_figure = Combobox(self._frame, 
                            values=[
                                    "None",
                                    "Dot", 
                                    "Cross",
                                    "Star",
                                    "Disc"])"""

        self._combo_figure.place(x=70, y = 20, width = 100, height= 20)
        self._combo_figure.bind("<<ComboboxSelected>>", self.figure_selected)

        #destroy old editor
        editor = globals['Int']

        editor = DotEditor.__class__.__name__(self._frame)
     #   editor = eval(DotEditor(self._frame ))
        print(editor)

    def figure_selected(self, event):
        print("selected", self._combo_figure.get())    


    def select_pad(self, pad):
        pass
from tkinter import Frame, Label
from tkinter.ttk import Combobox



class EventEditor:
    def __init__(self,  x_pos, y_pos, figures):
        self._frame = Frame( bg = "GRAY", borderwidth=1)  
        

        self._frame.config(highlightbackground = "RED", highlightcolor= "RED") 
        self._frame.place(height=400, width = 200, x=x_pos, y=y_pos)
        
        self._frame.bind("<ButtonRelease-1>", self.mouse_released)
        self._figure_list = figures

        self._actual_editor = None

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

     

        self._combo_figure.place(x=70, y = 20, width = 100, height= 20)
        self._combo_figure.bind("<<ComboboxSelected>>", self.figure_selected)


    def figure_selected(self, event):
        print("selected", self._combo_figure.get())    


        if self._actual_editor != None:
            self._actual_editor.destroy()

        self._actual_editor = self._figure_list[self._combo_figure.get()]
        
   
        self._actual_editor.create(self._frame)

   

    def set_pad(self, pad):
        self._combo_figure.set(pad.get_figure_name())

   
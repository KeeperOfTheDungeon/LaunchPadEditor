from tkinter import Frame

from Figure.Default.Default import Default



class PadEditor(Frame):
    def __init__(self, listener, pad, x_pos, y_pos):
        super().__init__(bg = "GRAY", borderwidth=1)
        self._pad = pad
        self._listener = listener 
        self._figure = Default(None, None)
        
        #self._frame = Frame( bg = "GRAY", borderwidth=1)  
        
        self.config(highlightbackground = "RED", highlightcolor= "RED") 
        self.place(height=70, width = 70, x=x_pos, y=y_pos)
        
        self.bind("<ButtonPress-1>", self.selected)
        self.bind("<ButtonRelease-1>", self.mouse_released)

        self.update()


    def selected(self, event):
        self._listener.pad_selected(self)


    def mouse_released(self, event):
        print("Mouse released")



    def get_figure_name(self):
        return self._figure.get_name()
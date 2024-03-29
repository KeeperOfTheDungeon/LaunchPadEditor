from tkinter import Frame

from Figure.Figure import Figure


class FigureEditor():
    def __init__(self):
        pass
        

    def create(self, root):
        self._frame = Frame( root, bg = "RED",  borderwidth=1)    
       
              
       # self._frame.config(highlightbackground = "RED", highlightcolor= "RED") 
        self._frame.place(height=70, width = 70, x=10, y=50)
        
    
        #self.bind("<ButtonRelease-1>", self.mouse_released)

        self._frame.update()


    def destroy(self):
        self._frame.place_forget()
        self._frame.destroy()        


    def init_figure(self):
        self._figure = Figure()

    def get_figure(self, figure):
        self._figure = figure

    def set_figure(self):
        return self._figure
from tkinter import Frame


class FigureEditor(Frame):
    def __init__(self, root):
        super().__init__(root, bg = "RED", borderwidth=1)
       
              
        self.config(highlightbackground = "RED", highlightcolor= "RED") 
        self.place(height=70, width = 70, x=10, y=30)
        
    
        #self.bind("<ButtonRelease-1>", self.mouse_released)

        self.update()
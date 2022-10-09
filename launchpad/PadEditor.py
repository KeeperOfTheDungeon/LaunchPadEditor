from tkinter import Frame



class PadEditor(Frame):
    def __init__(self, pad, x_pos, y_pos):
        super().__init__(bg = "GRAY", borderwidth=1)
        self._pad = pad
        #self._frame = Frame( bg = "GRAY", borderwidth=1)  
        
        self.config(highlightbackground = "RED", highlightcolor= "RED") 
        self.place(height=70, width = 70, x=x_pos, y=y_pos)
        
    
        self.bind("<ButtonRelease-1>", self.mouse_released)

        self.update()


    def mouse_released(self, event):
        print("Mouse released")




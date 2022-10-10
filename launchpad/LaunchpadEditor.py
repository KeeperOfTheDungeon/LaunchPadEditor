
import tkinter
from figure.Blink.BlinkEditor import BlinkEditor
from figure.Dot.DotEditor import DotEditor
from figure.disc.DiscEditor import DiscEditor
from launchpad.EventEditor import EventEditor

from launchpad.PadEditor import  PadEditor


class LaunchpadEditor:
    def __init__(self):
        self._frame = tkinter.Tk() 
        self._frame.title()
        self._frame.geometry("900x600")
        self._pad_list = list()

        for x_index in range (0,7):
            for y_index in range (0,7):
                editor = PadEditor(30, 20 + x_index*80, 20 + y_index*80)
                editor.bind("<ButtonPress-1>", self.editor_selected)
                self._pad_list.append(editor)


        figures = {"none" : 0,
                    "Disc" : DiscEditor(),
                    "Dot" : DotEditor(),
                    "Blink" : BlinkEditor()}


        self.event_editor = EventEditor(600,20, figures)

        self._frame.mainloop()
        
    def editor_selected(self, event):
        print ("ditor_selected")
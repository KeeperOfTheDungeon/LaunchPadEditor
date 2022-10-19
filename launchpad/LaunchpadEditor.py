
import tkinter
from Figure.Blink.Blink import Blink
from Figure.Blink.BlinkEditor import BlinkEditor
from Figure.Dot.DotEditor import DotEditor
from Figure.Dot.Dot import Dot
from Figure.Default.Default import Default
from Figure.Default.DefaultEditor import DefaultEditor
from Figure.Disc.Disc import Disc
from Figure.Disc.DiscEditor import DiscEditor
from Launchpad.EventEditor import EventEditor

from Launchpad.PadEditor import  PadEditor


class LaunchpadEditor:
    def __init__(self):
        self._frame = tkinter.Tk() 
        self._frame.title()
        self._frame.geometry("900x600")
        self._pad_list = list()

        for y_index in range (0,7):
            for x_index in range (0,7):
                editor = PadEditor(self, 30, 20 + x_index*80, 20 + y_index*80)
                #editor.bind("<ButtonPress-1>", self.editor_selected)
                self._pad_list.append(editor)


        figures = { Default._name : DefaultEditor(),
                    Disc._name : DiscEditor(),
                    Dot._name : DotEditor(),
                    Blink._name : BlinkEditor()}


        self.event_editor = EventEditor(600,20, figures)

        self._frame.mainloop()
        

    def pad_selected(self, pad):
        self.event_editor.set_pad(pad)
        print(pad)

    def editor_selected(self, event):
        print ("ditor_selected")
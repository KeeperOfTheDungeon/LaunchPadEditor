from figure.figure import Figure


class Star(Figure):
    def __init__(self, root, midi_out):
        self._clock_divider = 20
        self._root = root
        self._midi_out = midi_out
        self._phase = True
        self._is_active = False
        self._modulation = 127

    def midi_clock(self):
        self._clock_divider += 1
        if self._clock_divider > 5:
            self._phase = not self._phase
            self._clock_divider  = 0


        self.display()
        

    def get_root(self):
        return self._root


    def modulate(self, value):
        # modulate color
        # modulate brightness
        print("modulate")
        self._modulation = value
        pass    

    def start(self):
        self._is_active = True

    def end(self):

        self._is_active = False

    def display(self):
            
        center_red = 0
        center_green = 0 + self._modulation
        center_blue = 127

        outer_red = 127 - self._modulation 
    

        outer_green = 0 + self._modulation
        outer_blue = 0

        outer_red2 = int(outer_red/3)
        outer_green2 = int(outer_green/3)
        outer_blue2 = int(outer_blue/3)

        if self._is_active:
            if self._phase:
                message = [0xF0, 0x00, 0x20, 0x29, 0x02, 0x0E, 0x03, 
                            0x03, self._root,center_red,center_green,center_blue,
                            0x03, self._root+1,outer_red,outer_green,outer_blue,
                            0x03, self._root-1,outer_red,outer_green,outer_blue,
                            0x03, self._root+10,outer_red,outer_green,outer_blue,
                            0x03, self._root-10,outer_red,outer_green,outer_blue,

                            0x03, self._root+11,outer_red2,outer_green2,outer_blue2,
                            0x03, self._root-11,outer_red2, outer_green2,outer_blue2,
                            0x03, self._root+9,outer_red2, outer_green2,outer_blue2,
                            0x03, self._root-9,outer_red2, outer_green2,outer_blue2,
                            
                            0xf7]

            else:
                  message = [0xF0, 0x00, 0x20, 0x29, 0x02, 0x0E, 0x03, 
                            0x03, self._root,center_red,center_green,center_blue,

                            0x03, self._root+1,outer_red2,outer_green2,outer_blue2,
                            0x03, self._root-1,outer_red2,outer_green2,outer_blue2,
                            0x03, self._root+10,outer_red2,outer_green2,outer_blue2,
                            0x03, self._root-10,outer_red2,outer_green2,outer_blue2,

                            0x03, self._root+9,outer_red,outer_green,outer_blue,
                            0x03, self._root-9,outer_red,outer_green,outer_blue,
                            0x03, self._root+11,outer_red,outer_green,outer_blue,
                            0x03, self._root-11,outer_red,outer_green,outer_blue,

                            0xf7]

            self._midi_out.write_sys_ex(0, message)

            pass

            #self._midi_out.note_on(self._root, velocity=50, channel=0)
            #self._midi_out.note_on(self._root+10, velocity=100, channel=0)
            #self._midi_out.note_on(self._root-10, velocity=100, channel=0)
            #self._midi_out.note_on(self._root-1, velocity=100, channel=0)
            #self._midi_out.note_on(self._root+1, velocity=100, channel=0)
        else:
            self._midi_out.note_on(self._root, velocity=0, channel=0)
            self._midi_out.note_on(self._root+10, velocity=0, channel=0)
            self._midi_out.note_on(self._root-10, velocity=0, channel=0)
            self._midi_out.note_on(self._root-1, velocity=0, channel=0)
            self._midi_out.note_on(self._root+1, velocity=0, channel=0)

            self._midi_out.note_on(self._root+9, velocity=0, channel=0)
            self._midi_out.note_on(self._root-9, velocity=0, channel=0)
            self._midi_out.note_on(self._root-11, velocity=0, channel=0)
            self._midi_out.note_on(self._root+11, velocity=0, channel=0)

    def is_active(self):
        return(self._is_active)
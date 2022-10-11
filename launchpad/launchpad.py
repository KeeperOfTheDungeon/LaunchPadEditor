

import threading
from time import sleep
import pygame.midi as midi
from Figure.Blink.blink import Blink
from Figure.Star import Star
from Launchpad.PadList import PadList
from midi.MidiInput import MidiInput
from Launchpad.Pad import Pad


DEVICE_NAME = b'LPProMK3 MIDI'

class Launchpad:
    def __init__(self):

        #self._pads = [Pad(x) for x in range(0,109)]
        self._pads = PadList()
        self._activeFigures = list()
        
        self.init_midi()

        for pad in range (0 , self._pads.size()):
            self._pads.set_figure(pad, Star( pad, self._midi_out))


        
        self.set_program_mode()
        

        self._midi_out.set_instrument(0)
       

     #   for index in range (0,127):
      #      self._midi_out.note_on(note = 68, velocity=index, channel=0)
     #       sleep(.5)
     #       self._midi_out.note_off(note = 68, velocity=0, channel=0)

      #  for index in range (0,63):
      #      self._pads = Pad(1)

    

        self.running = True
        x = threading.Thread(target=self.run)
        x.start()



    def run(self):
        while self.running == True:
       
    # read midi
                
            sleep(0.001)



    def get_pad_list(self):
        return(self._pads)       


    def receive(self, message):
        
        received_data = message[0][0]

        command = received_data[0]

        if command == 0xf8:
            self.process_clock()

        if command >= 0xf0:
             #print("sysex")
             pass


        elif command >= 0xE0:
            print("PB")



        elif command >= 0xD0:
            self.process_pa(received_data)


        elif command >= 0xC0:
            print("pc")

        elif command >= 0xB0:
            self.process_cc(received_data)


        elif command >= 0xA0:
            self.process_pa(received_data)

        elif command >= 0x90:
            self.process_note_on(received_data)
        elif command >= 0x80:
            self.process_note_off(received_data)


    def process_clock(self):

        for figure in self._activeFigures:
            figure.midi_clock()
            if not figure.is_active():
                self._activeFigures.remove(figure)
        pass

    def process_pa(self, message):
        note = message [1]
        velocity = message [2]
        figure = self._pads.get_figure(note)
        figure.modulate(velocity)



    def process_note_on(self, message):
        print("No")
        note = message [1]
        velocity = message [2]
        print("Nf", note, " : ", velocity)
        pad = note - 11
        x = pad % 10
        y = int(pad / 10)
        print("xy", x, " : ", y)
        #self._midi_out.note_on(note = 0+x+y*10, velocity=velocity, channel=0)
       # self._midi_out.note_on(note, velocity=velocity, channel=0)
        
        if velocity >0:
            figure = self._pads.get_figure(note)
            figure.start()
            self._activeFigures.append(figure)
        else:   
            figure = self._pads.get_figure(note)
            figure.end()
        

            #self._activeFigures.append(Blink( note, self._midi_out))

    def process_cc(self, message):
        print("cc")
        note = message [1]
        velocity = message [2]
        print("Nf", note, " : ", velocity)
        pad = note - 11
        x = pad % 10
        y = int(pad / 10)
        print("xy", x, " : ", y)
        #self._midi_out.note_on(note = 0+x+y*10, velocity=velocity, channel=0)
        self._midi_out.note_on(note, velocity=velocity, channel=0)



    def process_note_off(self, message):
        note = message [1]
        velocity = message [2]
        print("Nf", note, " : ", velocity)


    def init_midi(self):
        
        midi.init()

        self._midi_input = MidiInput()
        self._midi_input.connect(midi, b'LPProMK3 MIDI')
        self._midi_input.set_receiver(self)


        deviceId = -1
        for testId in range(midi.get_count()):
    

    
            try:
                interf, deviceName, isInput, isOutput, opened = midi.get_device_info(testId)
                if deviceName == DEVICE_NAME and isOutput == 1:
                    deviceId = testId
                    print("MIDI-Gerät gefunden mit Id: " + str(deviceId))
                    print(midi.get_device_info(deviceId))
                    break

            except TypeError:
                pass    


        self._midi_out = midi.Output(deviceId)
        interf, deviceName, isInput, isOutput, opened = midi.get_device_info(deviceId)
        pass
      

    def set_program_mode(self):
        self._midi_out.write_sys_ex(0, [0xF0, 0x00, 0x20, 0x29, 0x02, 0x0E, 0x00, 0x11, 0x00, 0x00, 0xF7])


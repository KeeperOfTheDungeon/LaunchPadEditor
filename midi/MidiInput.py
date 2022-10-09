import threading
from time import sleep


class MidiInput:
    def __init__(self):
        self._receiver = None


    def set_receiver(self, receiver):
        self._receiver = receiver

    def connect(self, midi, device_name):

        deviceId = -1
        for testId in range(midi.get_count()):
    

    
            try:
                interf, deviceName, isInput, isOutput, opened = midi.get_device_info(testId)
                if deviceName == device_name and isInput == 1:
                    deviceId = testId
                    
                    print("MIDI-Gerät gefunden mit Id: " + str(deviceId))
                    print(midi.get_device_info(deviceId))
                    
                    self._midi_in = midi.Input(deviceId)
    
                    self.running = True
                    x = threading.Thread(target=self.run)
                    x.start()

                    break

            except TypeError:
                pass    


    
        #interf, deviceName, isInput, isOutput, opened = midi.get_device_info(deviceId)



        pass



    def run(self):
        while self.running == True:
       
    # read midi
            if self._midi_in.poll():
                message = self._midi_in.read(1)   
                if (self._receiver != None):
                    self._receiver.receive(message)
            else:
                sleep(0.001)
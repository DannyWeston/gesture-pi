import machine
import utime

from sensors import PhotoSensor, SonarSensor

import machine as ma
    
class App():
    def __init__(self):
        self.cpu_hz = 160000000
        ma.freq(self.cpu_hz)
        
        self.photo1 = PhotoSensor(pin_id = 26)
        self.photo2 = PhotoSensor(pin_id = 27)
        self.photo3 = PhotoSensor(pin_id = 28)
        self.sonar = SonarSensor(trigger_pin_id = 2, echo_pin_id = 3)
        
        self.photo1.start()
        self.photo2.start()
        self.photo3.start()
        self.sonar.start()
        
        self._start_time = 0

# Startup sequence
print("Application by DannyWeston")

app = App()

while True:
    print("Sonar: " + str(app.sonar.read_value()))
    print("Photo1: " + str(app.photo1.read_value()))
    print("Photo2: " + str(app.photo2.read_value()))
    print("Photo3: " + str(app.photo3.read_value()))
    utime.sleep(.1)
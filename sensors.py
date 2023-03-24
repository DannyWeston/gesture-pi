import machine as ma

from utilities import to_range

import utime

class Sensor():
    def __init__(self, rate):
        self.rate = rate
        
        self.timer = ma.Timer()
        
    def start(self):
        # Some clearup may be done
        #self.timer.init(freq=self.rate, mode=ma.Timer.PERIODIC, callback=self.read_value)
        pass
                
    def read_value(self):
        raise NotImplementedError()

class SonarSensor(Sensor):
    def __init__(self, echo_pin_id, trigger_pin_id, rate=20):
        super().__init__(rate=rate)
        
        self.echo_pin_id = echo_pin_id
        self.trigger_pin_id = trigger_pin_id
        
        self.echo_pin = ma.Pin(echo_pin_id, ma.Pin.IN)
        self.trigger_pin = ma.Pin(trigger_pin_id, ma.Pin.OUT)
        
        self.value = None
        
    def read_value(self):
        self.trigger_pin.low()
        utime.sleep_us(2)
        
        self.trigger_pin.high()
        utime.sleep_us(5)
        
        self.trigger_pin.low()
        
        while self.echo_pin.value() == 0:
            signaloff = utime.ticks_us()
            
        while self.echo_pin.value() == 1:
            signalon = utime.ticks_us()
            
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        self.value = distance
        return self.value
        
class PhotoSensor(Sensor):
    def __init__(self, pin_id, rate=20):
        super().__init__(rate=rate)
        
        self.pin_id = pin_id
        self.pin = ma.ADC(ma.Pin(pin_id))
        
        self.value = None
        
    def read_value(self):
        self.value = to_range(self.pin.read_u16(), 0, 65535, 0, 1024)
        return self.value
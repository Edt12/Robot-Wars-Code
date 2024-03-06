from machine import Pin,ADC,PWM
from time import sleep
import time
import utime
from machine import Pin
import drv8830pico

I2C_ID=0
I2C_ADDR1=0x65
I2C_ADDR2=0x60

sda=machine.Pin(8)
scl=machine.Pin(9)

pinUDS = 16

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class GroveUltrasonicRanger(object):
    def __init__(self, pinUDS):
        self.dio = Pin(pinUDS, Pin.IN)

    def _get_distance(self):
        self.dio.init(self.dio.OUT)
        self.dio.value(0)
        time.sleep_us(2)
        self.dio.value(1)
        time.sleep_us(5) 
        self.dio.value(0)

        self.dio.init(self.dio.IN)
        
        begin = time.time_ns()
#         wait for any previous pulse to end
        while self.dio.value():
            if ((time.time_ns() - begin) > 1000000000):
                return None

#         wait for the pulse to start
        while not self.dio.value():
            if ((time.time_ns() - begin) > 1000000000):
                return None
        pulseBegin = time.time_ns();

#         wait for the pulse to stop
        while self.dio.value():
            if ((time.time_ns() - begin) > 1000000000):
                return None
    
        pulseEnd = time.time_ns();

        distance = ((pulseEnd - pulseBegin) / 1000 / 29 / 2)    # cm
        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

Grove = GroveUltrasonicRanger
def main():

        
    drv = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR1, i2c_id=I2C_ID)
    drv2 = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR2, i2c_id=I2C_ID)

    #set voltage appropriate for your motor
    drv.SetVoltage(5)
    drv2.SetVoltage(5)

    fan= Pin(16, Pin.OUT)  
    motionSensorOne	= Pin(18, Pin.IN)
    motionSensorTwo = Pin(20,Pin.IN)
    distanceMeasure = Pin(16,Pin.IN)


    servoOne=PWM(Pin(27))
    servoTwo=PWM(Pin(28))
    servoValOne =0
    servoValTwo = 0
    sonar = GroveUltrasonicRanger(pinUDS)


    while True:
        print('{} cm'.format(sonar.get_distance()))
        print(str(distanceMeasure.value()) + "Distance Measure")
        if motionSensorOne.value() == 1:
                drv.Forward()
        else:
            drv.Brake()
              


        if motionSensorTwo.value() == 1:
            drv2.Forward()
        else:
            drv2.Brake()

              





if __name__ == '__main__':
    main()
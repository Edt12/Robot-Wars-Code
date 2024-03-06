import sys
import time
from machine import Pin

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
    sonar = GroveUltrasonicRanger(pinUDS)

    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(0.2) #1 

if __name__ == '__main__':
    main()
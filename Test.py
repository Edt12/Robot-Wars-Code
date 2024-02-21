from machine import Pin,ADC,PWM
from time import sleep
import utime

fan= Pin(16, Pin.OUT)  
motionSensorOne	= Pin(18, Pin.IN)
motionSensorTwo = Pin(20,Pin.IN)
distanceMeasure = Pin(16,Pin.IN)


servoOne=PWM(Pin(27))
servoTwo=PWM(Pin(28))
servoValOne =0
servoValTwo = 0

while True:
    
    print(str(distanceMeasure.value()) + "Distance Measure")
    if motionSensorOne.value() == 1:
            while  servoValOne<65535:
                servoValOne=servoValOne+1000
                utime.sleep_ms(1)
                servoOne.duty_u16(servoValOne)
            
            while servoValOne>0: 
                servoValOne=servoValOne-50
                utime.sleep_ms(1)
                servoOne.duty_u16(servoValOne)
              


    if motionSensorTwo.value() == 1:
            while  servoValTwo<65535:
                servoValTwo=servoValTwo+1000
                utime.sleep_ms(1)
                servoTwo.duty_u16(servoValTwo)
            
            while servoValTwo>0: 
                servoValTwo=servoValTwo-50
                utime.sleep_ms(1)
                servoTwo.duty_u16(servoValTwo)
           

          

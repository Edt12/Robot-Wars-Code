
import machine, time
from machine import Pin
import drv8830pico

I2C_ID=0
I2C_ADDR1=0x65
I2C_ADDR2=0x60

sda=machine.Pin(8)
scl=machine.Pin(9)

drv = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR1, i2c_id=I2C_ID)
drv2 = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR2, i2c_id=I2C_ID)

#set voltage appropriate for your motor
drv.SetVoltage(5)
drv2.SetVoltage(5)

#drive forward for 5 seconds
drv.Forward()
drv2.Forward()
time.sleep(1)
# 
# #stop and pause for a second
# drv.Brake()
# drv2.Brake()
# time.sleep(1)
# 
# #drive backwards for 5 seconds
# drv.Backward()
# drv2.Backward()
# time.sleep(1)
# 
# #coast to a stop
# drv.Coast()
# drv2.Coast()
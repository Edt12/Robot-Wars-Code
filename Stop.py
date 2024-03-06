from machine import Pin,ADC,PWM
from time import sleep
import utime
import drv8830pico

I2C_ID=0
I2C_ADDR1=0x65
I2C_ADDR2=0x60

sda=machine.Pin(8)
scl=machine.Pin(9)

drv = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR1, i2c_id=I2C_ID)
drv2 = drv8830pico.DRV8830(sda_pin=sda, scl_pin=scl, i2c_addr=I2C_ADDR2, i2c_id=I2C_ID)

#set voltage appropriate for your motor
drv.SetVoltage(3)
drv2.SetVoltage(3)

drv.Brake()
drv2.Brake()

miniFun = Pin(16, Pin.OUT)  
miniPir = Pin(18, Pin.IN)


pwm_Servo=PWM(Pin(27))
pwm_Servo.freq(500)
Servo_Val =0  
miniFun.value(0)
pwm_Servo.duty_u16(0)


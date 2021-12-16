#!/usr/bin/python3
import time
import board
import adafruit_adxl34x

class adxl345_interface:
    def __init__(self):
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.accelerometer = adafruit_adxl34x.ADXL345(self.i2c)

    def read_values(self):
        # gather values and return them as an array
        raw_values = self.accelerometer.acceleration
        # option to return as a dictionary
        # values = {'x' : raw_values[0], 'y' : raw_values[1], 'z' : raw_values[2]}
        return raw_values 

# implementation example
# adxl = adxl345_interface()
# while True:
#     values = adxl.read_values()
#     print(values)
#     #print("%f %f %f"%accelerometer.acceleration)
#     time.sleep(1)

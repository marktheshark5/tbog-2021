#!/usr/bin/python3
import board
import adafruit_ahtx0

class aht20_interface:
    def __init__(self):
        # Create sensor object, communicating over the board's default I2C bus
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.sensor = adafruit_ahtx0.AHTx0(self.i2c)
        
    def read_values(self):
        values = {'temp':self.sensor.temperature, 'humi':self.sensor.relative_humidity}
        return values



    



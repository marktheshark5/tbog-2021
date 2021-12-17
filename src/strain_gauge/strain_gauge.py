#!/usr/bin/python3

# code to interface with strain gauges
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from analog_in_diff import AnalogIn
# from adafruit_ads1x15.analog_in import AnalogIn

class strainGauge(): 
    def __init__(self):
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the ADC object using the I2C bus
        self.adc = ADS.ADS1115(i2c)
        # Create single-ended input on channel 0
        self.chan = AnalogIn(self.adc, ADS.P0)

    def readValue(self):
        # Create differential input between channel 0
        values = AnalogIn(self.adc, ADS.P0)
        return values

# # example implementation
sen = strainGauge()
while True:
    values = sen.readValue()
    print("{:>5}\t{:>5.3f}".format(values.value, values.voltage))
    time.sleep(1)

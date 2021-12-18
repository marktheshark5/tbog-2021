#!/usr/bin/python3

# code to interface with strain gauges
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class strainGauge: 
    def __init__(self, adcNum: int = 0):
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA)
        
        if adcNum == 0: 
            # Create the ADC object using the I2C bus
            self.adc = ADS.ADS1115(i2c) # using default slave I2C address 0x48 (ADDR to ground)
            # Create differential ADC
            self.chan = AnalogIn(self.adc, ADS.P0, ADS.P1)
        else: # address
            self.adc = ADS.ADS1115(i2c, address = 0x49) # ADDR pin pulled to 3V3
            self.chan = AnalogIn(self.adc, ADS.P2, ADS.P3)

    def readValue(self):
        # Create differential input between channel 0
        values = AnalogIn(self.adc, ADS.P0)
        return values

# # example implementation
# adc0 = strainGauge(adcNum = 0)
# adc1 = strainGauge(adcNum = 1)

# while True:
#     values = adc0.readValue()
#     print('sen0: ')
#     print("{:>5}\t{:>5.3f}".format(values.value, values.voltage))
#     time.sleep(1)
#     values = adc1.readValue()
#     print('sen1: ')
#     print("{:>5}\t{:>5.3f}".format(values.value, values.voltage))
#     time.sleep(1)

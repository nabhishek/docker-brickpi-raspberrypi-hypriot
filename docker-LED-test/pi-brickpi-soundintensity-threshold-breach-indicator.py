from __future__ import division
from BrickPi import *   #import BrickPi.py file to use BrickPi operations
import os

BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW   
BrickPi.SensorType[PORT_2] = TYPE_SENSOR_RAW #Sound Sensor

# BrickPi.SensorType[PORT_3] = TYPE_SENSOR_RAW
# BrkickPi.SensorType[PORT_4] = TYPE_SENSOR_RAW

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

soundIntensityPercentage = 0

Color_Sensor_Port = PORT_1    # Setup the sensor on Port 1.

# Booleans indicate which LED will Glow
red = False
green = True

acceptable_threshold_intensity = 10

# Setup acceptable sound intensity threshold, if environment variable indicating the threshold is not set then use default value of 10 %
try:
    print "INTENSITY_THRESHOLD: " + os.environ["INTENSITY_THRESHOLD"]
    acceptable_threshold_intensity = int(os.environ["INTENSITY_THRESHOLD"])
except KeyError:
    acceptable_threshold_intensity = 10

print "acceptable threshold intensity: " + acceptable_threshold_intensity

result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors

while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
    
    # Calculate sound intesity percentage
    inv = (1000 - BrickPi.Sensor[PORT_2])
    soundIntensity = inv / 1000
    soundIntensityPercentage = soundIntensity  * 100
    print BrickPi.Sensor[PORT_2], inv, soundIntensity, soundIntensityPercentage

    # decide which LED needs to be turned on 
    if green and soundIntensityPercentage > acceptable_threshold_intensity :
        BrickPi.SensorType[Color_Sensor_Port] = TYPE_SENSOR_COLOR_RED
        green = False
        red = True
        BrickPiSetupSensors()
        time.sleep(.1)     # sleep for 100 ms
    elif red and soundIntensityPercentage <=  acceptable_threshold_intensity :
        BrickPi.SensorType[Color_Sensor_Port] = TYPE_SENSOR_COLOR_GREEN
        red = False
        green = True
        BrickPiSetupSensors()
        time.sleep(.1)     # sleep for 100 ms

    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors


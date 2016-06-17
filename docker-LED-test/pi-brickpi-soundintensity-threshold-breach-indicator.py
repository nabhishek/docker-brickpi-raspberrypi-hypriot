from __future__ import division
from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW   #Set the type of sensor at PORT_1
BrickPi.SensorType[PORT_2] = TYPE_SENSOR_RAW
BrickPi.SensorType[PORT_3] = TYPE_SENSOR_RAW
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_RAW

BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

soundIntensityPercentage = 0

Color_Sensor_Port = PORT_1                                                                              # Setup the sensor on Port 1.
red = 0
green = 1

result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
while True:
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
    inv = (1000 - BrickPi.Sensor[PORT_2])
    soundIntensity = inv / 1000
    soundIntensityPercentage = soundIntensity  * 100
    print BrickPi.Sensor[PORT_2], inv, soundIntensity, soundIntensityPercentage
    if green == 1 and soundIntensityPercentage > 10 :
        BrickPi.SensorType[Color_Sensor_Port] = TYPE_SENSOR_COLOR_RED
        green = 0
        red = 1
    elif red == 1 and soundIntensityPercentage <= 10 :
        BrickPi.SensorType[Color_Sensor_Port] = TYPE_SENSOR_COLOR_GREEN
        red = 0
        green = 1
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
    BrickPiSetupSensors()
    time.sleep(.1)     # sleep for 100 ms

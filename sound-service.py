#!/usr/bin/env python
from __future__ import division
import web
import xml.etree.ElementTree as ET
# import BrickPi.py # Library to use Lego Minstorm sound sensor
from BrickPi import *   

# define REST API Route
urls = (
    '/soundintensity', 'list_users'
)

app = web.application(urls, globals())

# print " from outside function"
BrickPiSetup()  # setup the serial port for communication
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW   #Set the type of sensor at PORT_1
BrickPi.SensorType[PORT_2] = TYPE_SENSOR_RAW
BrickPi.SensorType[PORT_3] = TYPE_SENSOR_RAW
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_RAW
        
BrickPiSetupSensors()   #Send the properties of sensors to BrickPi

soundIntensityPercentage = 0

class list_users:
    def GET(self):
        print " in function"
        # BrickPiSetup()  # setup the serial port for communication

        while True:
            print " in whil"
            print BrickPi.Sensor[PORT_1], BrickPi.Sensor[PORT_2], BrickPi.Sensor[PORT_3], BrickPi.Sensor[PORT_4]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
            result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
            if not result :
                print "Print all Sensor Data"
                print BrickPi.Sensor[PORT_1], BrickPi.Sensor[PORT_2], BrickPi.Sensor[PORT_3], BrickPi.Sensor[PORT_4]     #BrickPi.Sensor[PORT] stores the value obtained from sensor
                result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
                # print BrickPi.Sensor[PORT_2]
                # print (1000 - BrickPi.Sensor[PORT_2])
                inv = (1000 - BrickPi.Sensor[PORT_2])
                soundIntensity = inv / 1000
                soundIntensityPercentage = soundIntensity  * 100
                print BrickPi.Sensor[PORT_2], inv, soundIntensity, soundIntensityPercentage
                break
            time.sleep(.1)
        print soundIntensityPercentage
        # return the sound intensity 
        return soundIntensityPercentage 


if __name__ == "__main__":
    app.run()

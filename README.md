## Sound Intensity Threshold Monitor
The sound intensity threshold monitor uses Raspberrypi (Using Hypriot image, and maninderjit/pi-brickpi docker container image)  and Brickpi (which controls Lego mindstorm sound and color/led sensors), and indicates that the sound intensity is above configured threshold by turning the RED led on.

## Overview
Solution Overview
![Solution Overview](https://raw.githubusercontent.com/maniSbindra/docker-brickpi-raspberrypi-hypriot/master/images/overview.jpg "Solution Overview")

## Note ! Brickpi configuration with Hypriot image
* The hypriot image is used for running docker container images on the brickpi. When using brickpi with hypriot image, I need to to make changes to the cmdline.txt, config.txt files as indicated on the Brickpi site, and you will need to modify the device-init.yml file to use your wifi network

## Setup
* Flash the SD with hypriot image http://blog.hypriot.com/downloads/. As mentioned above, replace the 3 files on the root of the SD card with the files under hypriot-image-config-files folder of this repository 

## Python Code 
* As indicated in the Docker file, code executed in the docker container is in the python file docker-LED-test/pi-brickpi-soundintensity-threshold-breach-indicator.py

### sample docker run command : 
* Setting threshold using environment variable :
**docker run -e INTENSITY_THRESHOLD=40 -d --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti maninderjit/pi-brickpi**

* With default sount intensity threshold :
**docker run -d --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti maninderjit/pi-brickpi**

## Note ! Regarding some of the files used
* Brickpi.py, ir_receiver_check.py, docker-LED-test files are from the Dexter BrickPi Repository (https://github.com/DexterInd/BrickPi).
* THe Base docker file, which was then modified, has been taken from the Hypriot repository (http://blog.hypriot.com/downloads/).

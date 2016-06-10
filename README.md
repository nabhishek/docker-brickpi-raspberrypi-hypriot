## When the container built using the default docker file (Dockerfile) is run , then LED Connected to the Brickpi, which in turn is connected to the raspberry pi turns on 

#### sample run command : docker run --device /dev/ttyAMA0:/dev/ttyAMA0 --device /dev/mem:/dev/mem --privileged -ti maninderjit/pi-brickpi

## Note ! Regarding some of the files used
* Brickpi.py, ir_receiver_check.py, docker-LED-test files are from the Dexter BrickPi Repository (https://github.com/DexterInd/BrickPi).
* THe Base docker file, which was then modified, has been taken from the Hypriot repository (http://blog.hypriot.com/downloads/).

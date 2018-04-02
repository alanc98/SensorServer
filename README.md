# SensorServer

Python ZeroMQ sensor server for Raspberry Pi and other IOT devices

Each device has it's own ZeroMQ REQ/REP (REQ = Request, REP = Reply) server written in Python. Each server accepts text commands to do something like take a picture or read sensor data, and it returns either the sensor data or just a reply that the command was accepted.  

Read more about ZeroMQ here:
http://zeromq.org/

# Servers provided
The servers currently are for:

- Raspberry Pi Camera - Accepts REQ messages to capture images, video clips, or timelapse sequences. It also sends updates for active videos and timelapses via PUB messages

- Pimoroni Enviro pHAT - Accepts REQ messages to deliver data from the various sensors, and to control the LED lights on the board. It sends REP messages with the data collected. It also accepts REQ messages to start PUB messages at the specified rate, so the data can be subscibed to. 

- Adafruit sensors - A couple of Adafruit breakout boards are supported including the TSL2561 LUX sensor, and the BMP180 temp/pressure sensor. This server has not been maintained, and provides minimal functionality.


# Message Formats
See the individual server directories for details on the message formats that are accepted and returned. Here is a simple example:
Request a picture from the Pi Camera server
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=STILL,CMD=CAPTURE,SIZE=1,VFLIP=TRUE,FILE=test1.jpg,SENSOR_REQ_END

Reply from camera
SENSOR_REP,DEV=PI_CAMERA,SUB_DEV=STILL,STATUS=OK|ERROR,SENSOR_REP_END

# Installation
In order to use this on a Raspberry Pi, you need to install the following:
- The sensor/device support python modules. In the case of the Pi Camera, everything seems to be installed in the latest Raspbian distribution. For the Enviro pHat server, you need to install the python module from Pimoroni. 
- Python ZeroMQ support ( sudo apt install python-zmq )

Check out the software by typing:
$ git clone https://github.com/alanc98/SensorServer.git 


# Startup at boot time
See the rc.local file for examples of how to start these servers up when the Pi boots

# GUI for remote operation
Each Server has (or will eventually have) a GUI to interact with it. The GUI is written in PyQt4. In order to use the GUI you will need:
- python-qt4 ( sudo apt install python-qt4 )

The GUI for the pi_camera server allows you to remotely command the camera to capture images, videos and timelapse sequences

If you want to develop a GUI for a new sensor, or change an existing GUI, you will need:
- python-qt4-dev ( sudo apt install python-qt4-dev )
( also dev tools for QT designer ) 
With the Python QT4 GUI, the user interface is designed with QT designer, then the python "Design" class is genrated using the piuic4 command. 


# 


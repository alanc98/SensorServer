from __future__ import print_function
import zmq
import time

#
# CAMERA_IP_ADDRESS is the address of the Raspberry Pi running the camera
# sensor server
#
# CAMERA_IP_ADDRESS = '192.168.0.246' 
CAMERA_IP_ADDRESS = '127.0.0.1' 

#
# The file name to save the image to on the Raspberry Pi
#
FILE_NAME = '/home/pi/Pictures/test_image2.jpg'

#
# Image size to capture.
#  '1' = 1024x768
#  '2' = 1920x1080
#  '3' = 2592x1944
#
IMAGE_SIZE = '1'

#
# Create the ZeroMQ socket and connect to the server
# 
print("Connecting to Sensor Server")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://' + CAMERA_IP_ADDRESS + ':5557')
print("Connected")

#
# Send the command to the camera server
#
socket.send('SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=STILL,CMD=CAPTURE,SIZE=2,VFLIP=FALSE,FILE=' + FILE_NAME + ',SENSOR_REQ_END')

#
# Get the response back from the server and print it
# You could check to see if there was an error by parsing the response back from the server
#
message = socket.recv()
print("Received Pi_Camera sensor reply:",message)

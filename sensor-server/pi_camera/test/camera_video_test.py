from __future__ import print_function
import zmq
import time
import sys

#
# Helper Function to setup a ZMQ subscription
#
def SubscribeToFilter(FilterText, SubSocket):
   if isinstance(FilterText, bytes):
      FilterText = FilterText.decode('ascii')
   SubSocket.setsockopt_string(zmq.SUBSCRIBE, FilterText)

print("Connecting to Sensor Server")
sys.stdout.flush()
context = zmq.Context()
#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5557")

# SUB socket to get status data
sub_socket = context.socket(zmq.SUB)
sub_socket.connect('tcp://localhost:5558') 
SubscribeToFilter('SENSOR_PUB',sub_socket)

print("Connected")
socket.send("SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=VIDEO,CMD=CAPTURE,SIZE=2,VFLIP=TRUE,DURATION=10,FILE=/home/pi/Desktop/testvid.h264,SENSOR_REQ_END")
message = socket.recv()
print("Received Pi_Camera sensor reply:",message)

for i in range (10):
  status_message = sub_socket.recv()
  print("Received Pi_Camera status message:",status_message) 
status_message = sub_socket.recv()
print("Received Pi_Camera status message:",status_message) 

time.sleep(5)

socket.send("SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=VIDEO,CMD=CAPTURE,SIZE=3,VFLIP=FALSE,DURATION=10,FILE=/home/pi/Desktop/testvid2.h264,SENSOR_REQ_END")
message = socket.recv()
print("Received Pi_Camera sensor reply:",message)

for i in range (10):
  status_message = sub_socket.recv()
  print("Received Pi_Camera status message:",status_message) 
status_message = sub_socket.recv()
print("Received Pi_Camera status message:",status_message) 


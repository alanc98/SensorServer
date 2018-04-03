Messages for the Raspberry Pi Camera 

# Capture a picture 

Send the following formatted string to capture a picture:
```
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=STILL,CMD=CAPTURE,SIZE=1,VFLIP=TRUE,FILE=test1.jpg,SENSOR_REQ_END
```
The Reply message from the server will be STATUS=OK, or STATUS=ERROR
```  
SENSOR_REP,DEV=PI_CAMERA,SUB_DEV=STILL,STATUS=OK|ERROR,SENSOR_REP_END
```

# Video Clip

Send the following message to capture a video clip
```
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=VIDEO,CMD=CAPTURE,SIZE=1,VFLIP=TRUE,FILE=test1.mp4,DURATION=10,SENSOR_REQ_END
```
When a multi-second video is being captured, the sensor server will send a PUB message indicating the second of the video
``` 
Document PUB message here
```

If you want to cancel an active video, send the following command
```
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=VIDEO,CMD=CANCEL,SENSOR_REQ_END
```

This is the status REPly message for camera commands
```
SENSOR_REP,DEV=PI_CAMERA,SUB_DEV=VIDEO,STATUS=OK|ERROR,SENSOR_REP_END
``` 

# Time Lapse

Send the following message to capture a timelapse sequence.

```
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=TIMELAPSE,CMD=CAPTURE,SIZE=1,VFLIP=TRUE,FILE_PRE=timelapse-,DELAY=10,FRAMES=10,SENSOR_REQ_END
```

Similar to the video, the server will send back a periodic PUB message. This message will be send for every frame, not once per second.
```
Document PUB message here
```

If you want to cancel an active timelapse, send the following command
```
SENSOR_REQ,DEV=PI_CAMERA,SUB_DEV=TIMELAPSE,CMD=CANCEL,SENSOR_REQ_END
```
This is the status REPly message for the timelapse commands
```
SENSOR_REP,DEV=PI_CAMERA,SUB_DEV=TIMELAPSE,STATUS=OK|ERROR,SENSOR_REP_END
```


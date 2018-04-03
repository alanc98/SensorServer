Sample Command Line Programs for the pi_camera_server.py sensor server 

# Software needed

In addition to python (I'm currently using 2.x, but will update to 3.x in the near future) you need to install python-zmq support. On the Raspberry Pi that is done with the following command:
```
$ sudo apt install python-zmq
```

# Capture a picture 

pi_cam_remote_pic.py is an example of sending an image capture REQ message to the pi_camera_server

```
$ python pi_cam_remote_pic.py
```


# use python3  and remove ROS Opencv Pacakages

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
#import opencv ,darkflow,numpy and time
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time


#configure the yolo model
option = {
    'model': 'cfg/tiny-yolo-voc.cfg',
    'load': 'bin/tiny-yolo-voc.weights',
    'threshold': 0.50,
    'gpu': 0.9
}
'''

option = {
    'model': 'cfg/yolo-voc.cfg',
    'load': 'bin/yolo-voc.weights',
    'threshold': 0.50,
    'gpu': 0.9
}

'''

#initialize the tenserflow 
tfnet = TFNet(option)
#assign the camera 0 (primary camera)
capture = cv2.VideoCapture(0)
#choose random colour for boxes
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

while (capture.isOpened()):
    stime = time.time()#copy the start time,used for fps calculation
    ret, frame = capture.read()#read the frame
    results = tfnet.return_predict(frame) #predict the objects in the frame
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y']) #get top left corner point
            br = (result['bottomright']['x'], result['bottomright']['y'])#get bottom right corner point 
            label = result['label']  #get the label name
            frame = cv2.rectangle(frame, tl, br, color, 2)#draw rectangle box on detected object
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)#put the text 
        cv2.imshow('frame', frame)#display the frame
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))#print fps
        if cv2.waitKey(1) & 0xFF == ord('q'):#press q button to quit
            break
    else:
        capture.release() #release the camera
        cv2.destroyAllWindows()#close all frames
        break

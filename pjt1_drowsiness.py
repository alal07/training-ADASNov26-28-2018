# import system dependencies packages
import sys
import time
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import cv2 #cv2 python extension module

face_cascade = cv2.CascadeClassifier('lbpcascade/lbpcascade_frontalface_improved.xml') #face cascade LBP file for face detection
'''
face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml') #face cascade file for face detection
'''
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml') #eye cascade file for eye detection





if face_cascade.empty():
        raise IOError('Unable to load the face cascade classifier xml file') #error handling

if eye_cascade.empty():
       raise IOError('Unable to load the eye cascade classifier xml file') #error handling


cam = cv2.VideoCapture(0) # 0 specifies that we are using first cam
ds_factor = 1 #ds=display scale to resize the frame
count = 0
iters = 0
while(True):
      start_time=time.time()
      ret, frame = cam.read()
      frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA) #cv2.INTER_AREA for shrinking
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Our operations on the frame come here
      faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 1.3=scaling factor,5=minimum neighbours
      for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #drawing rectangle with starting point and ending point, 2=thickness
        roi_gray = gray[y:y+h,x:x+w] # region of interest
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,2.1,7) # 2.1=scaling factor,7=minimum neighbours

        for (x_e,y_e,w_e,h_e) in eyes:
             cv2.rectangle(roi_color,(x_e,y_e),(x_e+w_e,y_e+h_e),(0,255,0),2) # (0,255,0)=green color, 2=thickness
        
        if len(eyes) == 0: # 0=eyes closed
          print "Eyes closed"

        else:
          print "Eyes open" # 1=eyes open
          
        count += len(eyes)
        iters += 1
        if iters ==5:
          iters = 0
          if count == 0:
            print "Drowsiness Detected!!!"
          count = 0
      cv2.imshow('frame', frame)  # Display the resulting frame
      #print('fps',format(1/(time.time()-start_time)))
      if cv2.waitKey(1) & 0xFF == ord('q'):#cv2.waitkey returns an 32bit integer value, the key input is an ASCII which is an 8bit      integer value.  So we only care about these 8bits & 0xFF is used to mask of all 8bits of the sequence
        break

cv2.release
cv2.destroyAllWindows()















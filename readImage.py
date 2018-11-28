import sys
import numpy as numpy
import cv2 
# Remove ros opencv packages 
#print(sys.path)
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
#load an color image as grayscale
img = cv2.imread('lena.png',1)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
	cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
	cv2.imwrite('messigray.png',img)
	cv2.destroyAllWindows()

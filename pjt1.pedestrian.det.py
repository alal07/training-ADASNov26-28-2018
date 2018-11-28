# import the necessary packages
import numpy as np
from imutils.object_detection import non_max_suppression
from imutils import paths
import cv2


#cap = cv2.VideoCapture(0) # 0 specifies that we are using first cam
cap = cv2.VideoCapture('test_videos/1.mp4')
ds_factor=1  #used to reduce the frame size

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while(True):
        ret, image = cap.read()
        #image=cv2.imread("test_pic/pic2.jpg")
        image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA) #cv2.INTER_AREA for shrinking
        orig=image.copy()
	rects,weights=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.05) 	# detect people in the image

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
 
	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
 

 
	# show the output images
	cv2.imshow("Before NMS", orig)
	cv2.imshow("After NMS", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):#cv2.waitkey returns an 32bit integer value, the key input is an ASCII which is an 8bit      integer value.  So we only care about these 8bits & 0xFF is used to mask of all 8bits of the sequence
            break


cv2.release
cv2.destroyAllWindows()

	

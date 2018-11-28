# import system dependencies packages
import sys
# Remove ros opencv packages 
#print(sys.path)
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


# import libraries of python OpenCV 
import cv2

#read input image 
img = cv2.imread("lena.png")
cv2.imshow('Original Image',img)

#convert bgr to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#show the gray scale image
cv2.imshow('gray-output', gray)


#crop the image for given x,y and w,h values
#crop_img = img[y:y+h, x:x+w]
crop_img = img[100:400, 100:300]

#show  the cropped image
cv2.imshow('cropped-output', crop_img)
#wait for a keyboard event
cv2.waitKey(0)





     


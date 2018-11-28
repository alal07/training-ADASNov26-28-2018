# import system dependencies packages
import sys
# Remove ros opencv packages 
#print(sys.path)
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


# import libraries of python OpenCV 
import cv2


 
# capture frames from a video

cap = cv2.VideoCapture('test/video1.avi')

#capture frames from a camera
#cap = cv2.VideoCapture(0)

# Trained XML classifiers describes features of cars we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frame = cap.read()
    # read photo asa frame
    #frame=cv2.imread('test/pic2.jpg')
     
    # convert from rgb to gray scale(Avoid noise and reduce computation task)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
 
    # Detects cars of different sizes in the input image
    # adjust scaleFactor ,minNeighbors 
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)
     
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
 
    # Display frames in a window 
    cv2.imshow('output', frame)
    # Wait for Esc key to stop
    if cv2.waitKey(1) == 27:
        break
 
# De-allocate any associated memory usage
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('test_videos/video1.mp4')

while(True):
    ret, img = cap.read()
    img_color = img

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Reduce noise level and fast img processing
    gray = cv2.GaussianBlur(img,(5,5),3)  #Reduce noise level
    edge = cv2.Canny(gray,1,150,3)#Canny edge detection
    #cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    #cv2.imshow('edge',edge)
    lines = cv2.HoughLinesP(edge,1,np.pi/180,100,1,10)#Hough transform on the image to detect lines
    
    
    if lines is None:
        lines = []

    for line in lines:
        for obj in line:
            #print obj
            [x1,y1,x2,y2] = obj  #x1,y1 is the first point of line;x2,y2 is the second line of point
            dx,dy = x2-x1,y2-y1    
            angle = np.arctan2(dy,dx) * (180/np.pi)  #calulate angle  of line and convert into degree format
            #print angle
            if abs(angle)>20:#for removing horizontal lines
                cv2.line(img_color,(x1,y1),(x2,y2),(0,255,0),2)

    
    img_bin = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    for line in lines:
        for obj in line:
            [x1,y1,x2,y2] = obj
            dx,dy = x2-x1,y2-y1
            angle = np.arctan2(dy,dx) * (180/np.pi)
            if abs(angle)>20:
                cv2.line(img_bin,(x1,y1),(x2,y2),(0,255,0),2)

   
    cv2.imshow('image',img_color)
    cv2.imshow('binaryimage',img_bin)
    if cv2.waitKey(1) == 27:
        break    
cap.release()
cv2.destroyAllWindows()


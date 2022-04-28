import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass

#Trackbar for HSV values

cv2.namedWindow('trackbar')
cv2.createTrackbar('min_hue','trackbar',0,179,nothing)
cv2.createTrackbar('min_sat','trackbar',0,255,nothing)
cv2.createTrackbar('min_val','trackbar',0,255,nothing)
cv2.createTrackbar('max_hue','trackbar',179,179,nothing)
cv2.createTrackbar('max_sat','trackbar',255,255,nothing)
cv2.createTrackbar('max_val','trackbar',255,255,nothing)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('min_hue', 'trackbar')
    l_s = cv2.getTrackbarPos('min_sat', 'trackbar')
    l_v = cv2.getTrackbarPos('min_val', 'trackbar')
    h_h = cv2.getTrackbarPos('max_hue', 'trackbar')
    h_s = cv2.getTrackbarPos('max_sat', 'trackbar')
    h_v = cv2.getTrackbarPos('max_val', 'trackbar')

    low = np.array([l_h,l_s,l_v])
    high = np.array([h_h,h_s,h_v])

    mask = cv2.inRange(hsv,low,high)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',result)
    key = cv2.waitKey(1)
    if key == ord('s'):
        thearray = [[l_h,l_s,l_v],[h_h,h_s,h_v]]
        np.save('penrange', thearray)
        break
    if key == 27:       # if Exc is pressed
        break

cap.release()
cv2.destroyAllWindows()

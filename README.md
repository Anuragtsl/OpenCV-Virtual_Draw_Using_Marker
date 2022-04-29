# OpenCV-Virtual_Draw_Using_Marker

In this project, I use [OpenCV]() in python to draw on the screen using a virtual pen i.e, any marker can be used to draw/erase using the technique of contour detection based on the mask of the desired colored target marker.

# WorkFlow

1. Find the HSV range of the target Marker/pen and save the values in a .npy file

2. Use the above values to start drawing in the main code

3. First, use color masking to get a mask of our colored pen/marker using the above HSV range.

4. Next, using contour detection detect and track the location of that pen,i.e get the x,y coordinates.

5. Next, draw a line by joining the x,y coordinates of pen’s previous location (location in the previous frame) with the new x,y points.

6. Add a feature to use the marker as an Eraser to erase unwanted lines.

7. Finally, add another feature to clear the entire Canvas/Screen.

# Preview

![Image1]()

![Image2]()


#Njoy!!

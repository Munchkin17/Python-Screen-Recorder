#importing the required packages
import pyautogui
import cv2
import numpy as np


#Specify resolution
resolution = (1920, 1080)

#Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

#Specify name of Output file
filename = "Recording.avi"

#Specify frames rate
fps = 60.0

#Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

#Create an Empty Window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    #Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    #Convert the screenshot to a numpy array
    frame = np.array(img)

    #Convert it form BRG(Blue Red Green) to RGB(Red Green Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Write it to the output file
    out.write(frame)

    #Display the recording screen
    cv2.imshow('Live', frame)

    #Stop recording when 'p' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

#Release the Video writer
out.release()

#Destroy all the windows
cv2.destroyAllWindows()


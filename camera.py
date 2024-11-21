import cv2
import numpy as np

cam_port = 0
cam = cv2.VideoCapture(cam_port) 
result, image = cam.read() 
  
if result: 

    cv2.imwrite("currentPhoto.png", image) 
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #HSV is hue saturation value
    lower_red = np.array([140, 80, 80])
    upper_red = np.array([255, 255, 255])
    mask_red = cv2.inRange(image_hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    for contour in contours:
        if cv2.contourArea(contour) > 400:  # Filter small contours if needed
            cv2.drawContours(image_hsv, [contour], -1, (0, 255, 0), 3)

    lower_yellow = np.array([12, 160, 150])
    upper_yellow = np.array([60, 255, 255])
    mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
    contours, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    for contour in contours:
        if cv2.contourArea(contour) > 400:  # Filter small contours if needed
            cv2.drawContours(image_hsv, [contour], -1, (255, 0, 0), 3)


    bitwiseOr = cv2.bitwise_or(cv2.img_yellow, cv2.img_red)
    cv2.imshow("test",bitwiseOr)
    cv2.waitKey(0) 
    cv2.destroyWindow("test") 

   
else: 
    print("No image detected. Please! try again") 
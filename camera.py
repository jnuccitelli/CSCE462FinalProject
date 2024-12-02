import cv2
import numpy as np

def map_contours_to_grid(contours, grid_shape, image_shape):
    grid = np.zeros(grid_shape, dtype=int)  
    rows, cols = grid_shape
    img_height, img_width = image_shape

    cell_height = img_height / rows
    cell_width = img_width / cols

    for contour in contours:
        if cv2.contourArea(contour) > 400:  
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"]) 
                cy = int(M["m01"] / M["m00"]) 

                col = int(cx / cell_width)
                row = int(cy / cell_height)

                if 0 <= row < rows and 0 <= col < cols:
                    grid[row, col] = 1  
    return grid


def CaptureBoard(cam):

    result, image = cam.read()

    if result:
        cv2.imwrite("currentPhoto.png", image)
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red = np.array([140, 80, 80])
        upper_red = np.array([255, 255, 255])
        mask_red = cv2.inRange(image_hsv, lower_red, upper_red)
        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        grid_red = map_contours_to_grid(contours_red, (6, 7), image.shape[:2]) 
        
        lower_yellow = np.array([12, 160, 150])
        upper_yellow = np.array([60, 255, 255])
        mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
        contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        grid_yellow = map_contours_to_grid(contours_yellow, (6, 7), image.shape[:2]) 


        combined_grid = grid_red + grid_yellow * 2 

        for contour in contours_red:
            if cv2.contourArea(contour) > 400:
                cv2.drawContours(image, [contour], -1, (0, 0, 255), 3)

        for contour in contours_yellow:
            if cv2.contourArea(contour) > 400:
                cv2.drawContours(image, [contour], -1, (0, 255, 255), 3)

        #cv2.imshow("Contours", image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return combined_grid

    else:
        print("No image detected. Please try again.")
        return -1


print(CaptureBoard())

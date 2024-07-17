#HOME TASK 2
import cv2 as cv
import numpy as np

def homeTask_two(image_size):
    box_sizes = int(size * 0.10)
    #top-left box
    cv.rectangle(img, (0,0), (int(box_sizes), int(box_sizes)), (0,0,0), -1)
    #top-right box
    cv.rectangle(img, (int(width-box_sizes),0), (int(width),int(box_sizes)), (255,0,0), -1)
    #bottom-left box
    cv.rectangle(img, (0,int(height-box_sizes)), (int(box_sizes), int(height)), (0,255,0), -1)
    #bottom-right box
    cv.rectangle(img, (int(width-box_sizes), int(height-box_sizes)), (int(width), int(height)), (0,0,255), -1)
    return 0

size = int(input("Enter size of Image: "))

img = np.zeros((int(size),int(size),3), np.uint8)
height, width = img.shape[:2]
img[:,:,0] = 255
img[:,:,1] = 255
img[:,:,2] = 255

homeTask_two(size)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
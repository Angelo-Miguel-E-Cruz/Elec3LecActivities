#HOME TASK 1
import cv2 as cv
import numpy as np

def number_one(box_size):
    height, width = img.shape[:2]
    center_height = height / 2
    center_width = width / 2
    cv.rectangle(img, (int(center_width - box_size), int(center_height - box_size)),
                 (int(center_width + box_size), int(center_height + box_size)), (255, 255, 255), -1)
    return 0

def number_two(box_sizes):
    height, width = img.shape[:2]
    img[:, :, 0] = 255
    img[:, :, 1] = 255
    img[:, :, 2] = 255
    # top-left box
    cv.rectangle(img, (0, 0), (int(box_sizes), int(box_sizes)), (0, 0, 0), -1)
    # top-right box
    cv.rectangle(img, (int(width - box_sizes), 0), (int(width), int(box_sizes)), (0, 0, 0), -1)
    # bottom-left box
    cv.rectangle(img, (0, int(height - box_sizes)), (int(box_sizes), int(height)), (0, 0, 0), -1)
    # bottom-right box
    cv.rectangle(img, (int(width - box_sizes), int(height - box_sizes)), (int(width), int(height)), (0, 0, 0), -1)
    return 0

def number_three(col_count, row_count, line_size):
    height, width = img.shape[:2]
    img[:, :, 0] = 255
    img[:, :, 1] = 255
    img[:, :, 2] = 255
    col_dst = int(size / (col_count + 1))
    row_dst = int(size / (row_count + 1))

    i = 1
    while i <= col_count:
        col_x = col_dst * i
        cv.line(img, (int(col_x), 0), (int(col_x), height), (0, 0, 0), int(line_size))
        i += 1

    j = 1
    while j <= row_count:
        row_y = row_dst * j
        cv.line(img, (0, int(row_y)), (width, int(row_y)), (0, 0, 0), int(line_size))
        j += 1
    return 0

size = int(input("Enter size of Image: "))

img = np.zeros((int(size), int(size), 3), np.uint8)

userInput = int(input("Choose Number to Show: "))
if userInput == 1:
    small_size = int(input("Enter size of Box: "))
    number_one(small_size)
elif userInput == 2:
    small_box = int(input("Enter size of Boxes: "))
    number_two(small_box)
elif userInput == 3:
    col_num = int(input("Enter number of columns: "))
    row_num = int(input("Enter number of rows: "))
    line_px = int(input("Enter line thickness: "))
    number_three(col_num, row_num, line_px)
else:
    print("Invalid Input")
    exit()

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
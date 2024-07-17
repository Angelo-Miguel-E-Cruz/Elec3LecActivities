# LAB 2
import cv2
import matplotlib.pyplot as plt
import numpy as np

#read image
'''image = cv2.imread("image.jpeg", 0)
height, width = image.shape[:2]

#number 1
crop_img = image[81:159, 0:318]
rows, cols = crop_img.shape
flip_img = cv2.flip(crop_img, 0)
mirror_img = np.vstack((crop_img,flip_img))

#number 2
x_borders = width * 0.10
new_size = width + x_borders
y_borders = (new_size - height)/2
border = cv2.copyMakeBorder(image, int(y_borders), int(y_borders), int(x_borders), int(x_borders),cv2.BORDER_CONSTANT, value=[0, 0, 0])
'''
#number 3
i = int(input("Enter First Number: "))
j = int(input("Enter Second Number: "))
x = np.arange(-i, j, 1)
X, Y = np.meshgrid(x, x)

wavelength = 200
angle = np.pi/9
f = np.sin(2 * np.pi * (X*np.cos(angle) + Y*np.sin(angle))/ wavelength)

plt.set_cmap("gray")
plt.imshow(f)
plt.show()

#show images
'''cv2.imshow("Image", image)
cv2.imshow("Mirror", mirror_img)
cv2.imshow("Border", border)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
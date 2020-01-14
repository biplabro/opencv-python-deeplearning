#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:11:47 2020

@author: roy
"""
# import libraries
import cv2
import numpy as np

# import image
image = cv2.imread('p03.jpg')

# BGR values for (x,y)th pixel
B, G, R = image[11, 75]
print ('(x,y)th pixel intensity or RGB image', B, G, R)
print ('shape of original image', image.shape)

# convert image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print ('gray_image_shape', gray_img.shape)
# print pixel intensity of B/W image 
print ('(x,y)th pixel intensity or grayscale image', gray_img[11, 75])
cv2.imshow('grayscale_image', gray_img)
cv2.waitKey(0)
cv2.imwrite('grayscale_image.jpg', gray_img)

# image manipulation in HSV color space
# channel H: 0 - 180, S: 0 - 255, V: 0 - 255
# image = cv2.imread('p04.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
H, S, V = hsv_image[11,75]
print ('HSV Value', H, S, V)
print ('hsv_image_shape', image.shape)

cv2.imshow('HSV image', hsv_image)
# hsv_image[length: width: colorspace h, s and v represented by 0, 1 and 2]
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

# wait for keystroke & close all image windows
cv2.waitKey(0)
#cv2.destroyAllWindows()

# save the output images
cv2.imwrite('Hue channel.jpg', hsv_image[:, :, 0])
cv2.imwrite('Saturation channel.jpg', hsv_image[:, :, 1])
cv2.imwrite('Value channel.jpg', hsv_image[:, :, 2])

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)

#print(B.shape)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# save BGR channel of images
cv2.imwrite("Red.jpg", R)
cv2.imwrite("Green.jpg", G)
cv2.imwrite("Blue.jpg", B)

cv2.waitKey(0)
#cv2.destroyAllWindows()

# Let's re-make the original image, 
merged = cv2.merge([B, G, R]) 
cv2.imshow("Merged", merged) 
cv2.imwrite("Merged.jpg", merged) 

# Let's amplify the red color
merged = cv2.merge([B, G, R+66])
cv2.imshow("Merged with Red Amplified", merged) 
cv2.imwrite("Merged with Red Amplified.jpg", merged) 

cv2.waitKey(0)
#cv2.destroyAllWindows()

B, G, R = cv2.split(image)

# Let's create a matrix of zeros 
# with dimensions of the image h x w  
zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red-Zero", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green-Zero", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue-Zero", cv2.merge([B, zeros, zeros]))

cv2.imwrite("Red-Zero.jpg", cv2.merge([zeros, zeros, R]))
cv2.imwrite("Green-Zero.jpg", cv2.merge([zeros, G, zeros]))
cv2.imwrite("Blue-Zero.jpg", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
image.shape[:2]


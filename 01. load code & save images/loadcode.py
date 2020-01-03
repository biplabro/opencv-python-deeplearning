#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 20:54:43 2020

@author: roy
"""

#import modules
import cv2
import numpy as np #np can be any random name

#Input image
input = cv2.imread('p01.jpg')

#Basic operations on image like checking the dimensions & colorspace
cv2.imshow('first_image', input)
cv2.waitKey()
cv2.destroyAllWindows()

#output the data
print(input.shape)
print('Image Height', int(input.shape[0]), 'pixels')
print('Image width', int(input.shape[1]), 'pixels')
print('Image color', int(input.shape[2]), 'types')

#save the output image, no manipulation on the source image is done though 
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:00:42 2020

@author: roy
"""
#Method-1
#========

#library import
import cv2

#load image
image = cv2.imread('p02.jpg')
cv2.imshow('color image', image)
cv2.waitKey()

#process image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

#store image
cv2.imwrite('Grayscaled.jpg', gray_image)

#Method-2
#========





# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:37:27 2018

@author: Administrator
"""
import cv2
import numpy as np

img = cv2.imread("1.jpg")
scale = 1 # if original image is two big set it to lower than 1
block = 8  # character size
img = cv2.resize(img,(int(img.shape[0]*scale),int(img.shape[1]*scale)),interpolation=cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.equalizeHist(gray)  
ascii_img = gray
ascii_img = cv2.resize(ascii_img,(int(gray.shape[0]*block),int(gray.shape[1]*block)),interpolation=cv2.INTER_CUBIC)
ascii_img[:,:] = 255
characters = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            index = int(gray[i,j]/(256./70.))
            cv2.putText(ascii_img, characters[index], (block*j,block*i), cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)

cv2.imwrite("ascii_img.jpg",ascii_img)

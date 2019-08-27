# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:56:49 2019

@author: Abhi
"""

from matplotlib import pyplot as plt
from skimage.feature import blob_log
from math import sqrt
from skimage.color import rgb2gray
from skimage.io import imread



im = imread("C://Users//Abhi//Desktop//wint_sky.jpg")
plt.imshow(im)
image_gray = rgb2gray(im)

blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)

fig, ax = plt.subplots(1, 1)
plt.imshow(im)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)
    

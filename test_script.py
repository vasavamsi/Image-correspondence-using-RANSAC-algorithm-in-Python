# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:43:15 2020

@author: ADMIN-PC
"""

from image_reconstruction import reconstruct

# Taking the input from user
img_pair = int(input('enter the image pair no. from 1 to 5: ')) #change the as per given sets of images
path = './img_pair_' + str(img_pair) + '/'

#Calling the function
reconstruct(path)


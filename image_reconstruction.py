# -*- coding: utf-8 -*-
"""
Created on Thurs Mar 24 23:20:14 2020

@author: ADMIN-PC
"""
import cv2 as cv
from ransac import RANSAC
import numpy as np
from numpy.linalg import norm

def reconstruct(path):
    ## Taking the first image
    file_name = path + '1.jpg'
    img = cv.imread(file_name)
    img_1 = cv.resize(img, None, fx=0.25, fy=0.25) ##Comment if downscaling is not desired
    img_1_gray = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
    
    ##Taking in the second image
    file_name = path + '2.jpg'
    img = cv.imread(file_name)
    img_2 = cv.resize(img, None, fx=0.25, fy=0.25)
    img_2_gray = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
    
    ## Getting Fundamental Matrix using RANSAC Algorithm
    F = RANSAC(img_1, img_2)
    print('the Fundaamental Matrix obtained is as follows:')
    print(F)
    print('==============================================================================================================')
    print('initializing the image reconstruction')
    
    # Generating the reference image from the source image
    canvas = np.zeros((img_1.shape))
    patch_size = input('the patch size to be taken:')
    mid = int(round(patch_size/2))
    cnt = 0
    
    # Taking patch from the reference image
    for y in range(mid, img_1.shape[0]-mid, patch_size):
        for x in range(mid, img_1.shape[1]-mid, patch_size):
            X = np.array([[x],[y],[1]])
            epi_line = np.dot(F,X)
            epi_line = epi_line/epi_line[2]
            r_patch_vec = np.reshape(img_1_gray[y-mid:y+mid+1, x-mid:x+mid+1], (1,patch_size**2))
            
            # Getting Patch in source image using L2 norm
            min_diff = 10e+30
            for x_ in range(mid, img_2.shape[1]-mid+1):
                y_ = -(epi_line[0]*x_ + 1)/epi_line[1]
                if y_ >= mid and y_ <= img_2.shape[0]-mid and y_ >= y-100 and y_ <= y+100:
                    s_patch = img_2_gray[int(y_)-mid:int(y_)+mid+1, x_-mid:x_+mid+1]
                    if s_patch.shape[0]*s_patch.shape[1] != patch_size **2:
                        continue
                    else:
                        s_patch_vec = np.reshape(img_2_gray[int(y_)-mid:int(y_)+mid+1, x_-mid:x_+mid+1], (1,patch_size**2))                
                        diff = norm(r_patch_vec- s_patch_vec)
                        
                    if diff <= min_diff:
                        s_fin_patch = img_2[int(y_)-mid:int(y_)+mid+1, x_-mid:x_+mid+1,:]
                        min_diff = diff
                    # Pasting the Patch in Canvas
                    canvas[y-mid:y+mid+1, x-mid:x+mid+1, :] = s_fin_patch
                    
                    # Saving the image
                    cv.imwrite(path + 'final_img.jpg', canvas)   
            cnt += 1
            if cnt % 100 == 0:
                print('patches completed :' + str(cnt))

    print('The image is reconstructed nd saved the following path ' + path)

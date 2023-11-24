# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:50:34 2020

@author: ADMIN-PC
"""
import cv2 as cv
import pandas as pd
import numpy as np
from numpy.linalg import norm
from fundamental_matrix import fundamental_matrix
import random

def RANSAC(img_1, img_2):
    ##Taking care of the detector, i.e SIFT detector
    det = cv.xfeatures2d.SIFT_create()
    
    #Getting keypoints and their feature descriptor for first image
    kp1, des1 = det.detectAndCompute(img_1, None)
    des1 = np.array(des1, dtype = "float32")

    #Getting keypoints and their feature descriptor for first image
    kp2, des2 = det.detectAndCompute(img_2, None)
    des2 = np.array(des2)
    
    # key point matching
    coord1 = []
    coord2 = []
    dist_list = []
    for i in range(des1.shape[0]):
        diff_mat = des1[i,:] - des2
        dist =  norm(diff_mat, axis = 1)
        k2 = np.argmin(dist)
        coord1.append(kp1[i].pt)
        coord2.append(kp2[k2].pt)
        dist_list.append(np.min(dist))
##########################################################################################################
#   Calculating Fundamental matrix using inbuilt function
    F_inbuilt = cv.findFundamentalMat(np.float32(coord1), np.float32(coord2), method=cv.FM_7POINT)
    print('Fundamental matrix using inbuilt function')
    print(F_inbuilt[0])
##########################################################################################################
    dist_df = pd.DataFrame(dist_list)
    dist_df = dist_df[0].sort_values()

    ##RANSAC Algorithm
    N = 10000 ## Can be changed as per user requirement
    Si_list = []
    n_inliers_list = []
    for iteration in range(0,N):
        # randomly sampling the 8 key points and determining the fundamental matrix
        rand_samples = random.sample(dist_df.index[:50], 8)
        
        x1 = []
        x2 = []
        y1 = []
        y2 = []
        for i in rand_samples:
            x1.append(coord1[i][0])
            x2.append(coord2[i][0])
            y1.append(coord1[i][1])
            y2.append(coord2[i][1])
        
        # Getting Fundamental Matrix for the Random Sample
        F = fundamental_matrix(x1,x2,y1,y2,img_1.shape[0],img_1.shape[1],img_2.shape[0],img_2.shape[1])
        
        # Getting the no. of inliers
        n_inliers = 0
        Si = []
        for n in dist_df.index[:50]:
            X = np.array([[coord1[n][0]], [coord1[n][1]], [1]])
            X_ = np.array([[coord2[n][0]], [coord2[n][1]], [1]])
            ep_criteria = np.dot(F, X)
            ep_criteria = np.dot(X_.T,ep_criteria)
            if abs(ep_criteria) < 10e-5:
                Si.append(n)
                n_inliers += 1
        Si_list.append(Si)
        n_inliers_list.append(n_inliers)
        if n_inliers >= 10:  ## Can be changes as per user requirement
            break
                
    print("RANSAC Algorithm stopped at " + str(iteration))
    print("Maximum no. of inliers obtained are " + str(max(n_inliers_list)))
    
    #Getting the final fundamental matrix    
    index = np.argmax(np.array(n_inliers_list))
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in Si_list[index]:
        x1.append(coord1[i][0])
        x2.append(coord2[i][0])
        y1.append(coord1[i][1])
        y2.append(coord2[i][1])
        
    F = fundamental_matrix(x1,x2,y1,y2,img_1.shape[0],img_1.shape[1],img_2.shape[0],img_2.shape[1])
    
    return F

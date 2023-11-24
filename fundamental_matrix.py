# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:26:16 2020

@author: ADMIN-PC
"""
import numpy as np

def fundamental_matrix(x1,x2,y1,y2,M1,N1,M2,N2):
    """
    Arguments:
        
    x1 = array of x-coordinates of the randomly sampled keypoints in first image
    x2 = array of x-coordinates of the randomly sampled keypoints in second image
    y1 = array of y-coordinates of the randomly sampled keypoints in first image
    y2 = array of y-coordinates of the randomly sampled keypoints in second image
    
    M1 = dimensionn of rows in the first image
    N1 = dimensionn of columns in the first image
    M2 = dimensionn of rows in the second image
    N2 = dimensionn of columns in the second image
    
    Returns:
        
    F = Fundamental Matrix
    """
    
    # Finding the fundamental matrix
            
    ## Normalizing the co-ordinates:
    # For image 1
    X1 = (float(2)/float(N1))*np.array(x1) - float(N1)/float(2)
    Y1 = (float(2)/float(M1))*np.array(y1) - float(M1)/float(2)
    
    # For image 2
    X2 = (float(2)/float(N2))*np.array(x2) - float(N2)/float(2)
    Y2 = (float(2)/float(M2))*np.array(y2) - float(M2)/float(2)
    
    # the T matrices
    T1 = np.matrix([[float(2)/float(N1), 0, -N1/2], [0, float(2)/float(M1), -M1/2], [0, 0, 1]])
    T2 = np.matrix([[float(2)/float(N2), 0, -N2/2], [0, float(2)/float(M2), -M2/2], [0, 0, 1]])
        
    ## Constructing A matrix
    A = np.matrix([])
    for n in range(len(x1)):
        Anew = np.matrix([[X1[n]*X2[n], Y1[n]*X2[n], X2[n], X1[n]*Y2[n], Y1[n]*Y2[n], Y2[n], X1[n], Y1[n], 1]])
        if n == 0:
            A = Anew
        else:
            A = np.concatenate((A,Anew))
    
    # Fundamental matrix without normalization
    U,S,V = np.linalg.svd(A)
    F = np.reshape(V[-1,:], (3,3))
    Fp = F/F[2,2]
    
    # Getting Actual homography estimation
    F = np.dot(Fp,T1)
    Fp = np.dot(T2.T,F)
    Fp = Fp/Fp[2,2] ##Actual homography estimation
    
    # Taking the SUV decomosition to reduce the rank
    U,S,V = np.linalg.svd(Fp)
    S[-1] = 0
    F = np.dot(U, np.diag(S))
    F = np.dot(F,V)

    return F

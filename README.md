## Image-correspondence-using-RANSAC-algorithm-in-Python
This work is completed as a part of Course assignment in 3D Computer Vision at IIT Gandhinagar

# Step by Step Algorithm

_Step 1_- The Code intake the images in the pair set entered by the user.

_Step 2_- The Fundamental Matrix is estimated using the RANSAC Algorithm (using both inbuilt and from scratch function) and displayed.

_Step 3_- The observation here is that although the fundamental matrices for both functions are fairly dissimilar, we can see that patch reconstruction is pretty well using from scratch function. Although, the inbuilt function is using the default parameters for param1 and param2 arguments.

_Step 4_- The no. of iterations here taken are limited to 10,000 but the original value to get 0.99 of probability exceeds 120*10^4 iterations. And the probability for being inliers is taken as 0.2.

_Step 5_- After getting the fundamental matrix the patch size for reconstruction is chosen by the user from 3 or 5, for better results. (Here all the results are obtained using 3).

_Step 6_- The blank canvas of size of ref image is defined and using fundamental matrix for each co-ordinate in ref image the epipolar line is obtained.

_Step 7_- The co-ordinates corresponding to the similar patch in reference image is obtained by fixing the co-ordinate in one axis and calculating the other using line equation.

_Step 8_- The similarity is checked using L2 norm (any other method like cosine similarity can also be used).

_Step 9_- After getting the source patch with least distance the patch is placed at the reference co-ordinate in canvas defined.

# Instructions to run code

1) Run test_script.py.
2) Enter the image pair no. to execute the code on respective set.(we have provided only one set with this repo so go for '1' as input)
3) The Fundamental matrix in between the pair of images will be displayed (both for inbuilt function and using my RANSAC function)
4) Input the image patch size (choose in between 3 and 5) for reconstruction.
5) The code is designed to save the intermediate progress to monitor and the no. of reconstructed patches is displayed at every 100 patches.
6) Final reconstructed image is saved in the same folder as of the image pair.

Here the Scene-1 is obtained using the 3 channelled (i.e RGB) reference and source patch and at regular size as of image. Due to the time constraint, the size is reduced in remaining scenes and Grayscale patches are used. In Scene-5, the patch size of 5 is used. The similarity metric of Cosine similarity is also used on one of the dataset for my understanding but not mentioned here, but the results were more of similar.

**Note:-**
The root directory is to be maintained as seen and naming of the images and their folders to be followed in the same fashion.

The resize function is used to downscale the image before considering for the RANSAC Algorthim and for reconstruction purpose due to time constraint. The same can uncommented for regular size reconstruction, but will consume more time.(same is mentioned in the image_reconstruction.py)

The no. of inliers in the ransac.py script can be changed to get the better Fundamental matrix.

The no. of iterations for the RANSAC Algorithm can also be changed as per user requirement.

(Both the above are commented in the code itself)
To see the intermediate progress, uncomment the part mentioned in panaroma_stitching.py.

(the intermediate images will be saved in the same directory in BGR format)
The parameters for RANSAC Algorithm in inbuilt fundamental matrix function is set for the default values.

**References:**
For Fundamental Matrix: Class Notes

For RANSAC Algorithm: Class Notes
https://engineering.purdue.edu/kak/courses-i-teach/ECE661.08/solution/hw4_s1.pdf

For inbuilt Fundamental Matrix Function: Open CV Documentation
https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#Mat%20
findFundamentalMat(InputArray%20points1,%20InputArray%20points2,%20int%20method,%20double%20par
am1,%20double%20param2,%20OutputArray%20mask)

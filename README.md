## Image-correspondence-using-RANSAC-algorithm-in-Python
This work is completed as a part of Course assignment in 3D Computer Vision at IIT Gandhinagar

# Step by Step Algorithm

Step 1- The Code intake the images in the pair set entered by the user.

Step 2- The Fundamental Matrix is estimated using the RANSAC Algorithm (using both inbuilt and from scratch function) and displayed.

Step 3- The observation here is that although the fundamental matrices for both functions are fairly dissimilar, we can see that patch reconstruction is pretty well using from scratch function. Although, the inbuilt function is using the default parameters for param1 and param2 arguments.

Step 4- The no. of iterations here taken are limited to 10,000 but the original value to get 0.99 of probability exceeds 120*10^4 iterations. And the probability for being inliers is taken as 0.2.

Step 5- After getting the fundamental matrix the patch size for reconstruction is chosen by the user from 3 or 5, for better results. (Here all the results are obtained using 3).

Step 6- The blank canvas of size of ref image is defined and using fundamental matrix for each co-ordinate in ref image the epipolar line is obtained.

Step 7- The co-ordinates corresponding to the similar patch in reference image is obtained by fixing the co-ordinate in one axis and calculating the other using line equation.

Step 8- The similarity is checked using L2 norm (any other method like cosine similarity can also be used).

Step 9- After getting the source patch with least distance the patch is placed at the reference co-ordinate in canvas defined.

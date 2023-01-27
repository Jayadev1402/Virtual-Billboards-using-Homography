import numpy as np
from est_homography import est_homography


def warp_pts(X, X_prime, interior_pts):
    """
    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
        interior_pts: Nx2 matrix of points inside goal
    Returns:
        warped_pts: Nx2 matrix containing new coordinates for interior_pts.
        These coordinate describe where a point inside the goal will be warped
        to inside the penn logo. 

    """


    H = est_homography(X, X_prime)


    warp=[]

    for i in range(0,interior_pts.shape[0]):
        [x,y,z]=H@[interior_pts[i,0],interior_pts[i,1],1]

        [xp,yp]=[x/z,y/z]
        warp.append([xp,yp])
        
    warped_pts = np.array(warp)
    return warped_pts

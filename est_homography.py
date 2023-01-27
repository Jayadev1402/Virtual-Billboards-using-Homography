import numpy as np

def est_homography(X, X_prime):
    """
    Calculates the homography of two planes, from the plane defined by X
    to the plane defined by X_prime. In this assignment, X are the coordinates of the
    four corners of the soccer goal while X_prime are the four corners of the penn logo

    Input:
        X: 4x2 matrix of (x,y) coordinates of goal corners in video frame
        X_prime: 4x2 matrix of (x,y) coordinates of logo corners in penn logo
    Returns:
        H: 3x3 homogeneours transformation matrix s.t. X_prime ~ H*X

    """

    ##### STUDENT CODE START #####
    H=np.zeros((8,9))
    for i in range(0,4):
        H[2*i,0]=-X[i,0]
        H[2*i,1]=-X[i,1]
        H[2*i,2]=-1
        H[2*i,3]=0
        H[2*i,4]=0
        H[2*i,5]=0
        H[2*i,6]=X[i,0]*X_prime[i,0]
        H[2*i,7]=X[i,1]*X_prime[i,0]
        H[2*i,8]=X_prime[i,0]

        H[2*i+1,0]=0
        H[2*i+1,1]=0
        H[2*i+1,2]=0
        H[2*i+1,3]=-X[i,0]
        H[2*i+1,4]=-X[i,1]
        H[2*i+1,5]=-1
        H[2*i+1,6]=X[i,0]*X_prime[i,1]
        H[2*i+1,7]=X[i,1]*X_prime[i,1]
        H[2*i+1,8]=X_prime[i,1]
        
    [u,s,vt]=np.linalg.svd(H)
    v=np.transpose(vt)
    h=v[:,-1]
    A=h.reshape(3,3)
    ##### STUDENT CODE END #####
    return A


# Virtual Billboard


## Description

This project utilizes the concepts of projective geometry and homographies to project an image (in this case, the Penn Engineering logo) onto a scene (a football goal) in a natural way that respects perspective.

The project includes images from a video sequence of a football match, as well as the corners of the goal in each image and an image of the Penn Engineering logo.

The task is to, for each image in the video sequence, compute the homography between the Penn logo and the goal, and then warp the goal points onto the ones in the Penn logo to generate a projection of the logo onto the video frame.

![](https://user-images.githubusercontent.com/89912646/215006062-6ce2f078-a67e-4a45-885b-4063fc8c1418.png | width=100)



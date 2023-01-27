# Virtual Billboard


## Description

This project utilizes the concepts of projective geometry and homographies to project an image (in this case, the Penn Engineering logo) onto a scene (a football goal) in a natural way that respects perspective.

The project includes images from a video sequence of a football match, as well as the corners of the goal in each image and an image of the Penn Engineering logo.

The task is to, for each image in the video sequence, compute the homography between the Penn logo and the goal, and then warp the goal points onto the ones in the Penn logo to generate a projection of the logo onto the video frame.

![plot](./Jayadev1402/demo/part_1_results/frame0.png)


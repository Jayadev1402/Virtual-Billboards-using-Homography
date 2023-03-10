# Virtual Billboard


## Description

This project utilizes the concepts of projective geometry and homographies to project an image (in this case, the Penn Engineering logo) onto a scene (a football goal) in a natural way that respects perspective.

The project includes images from a video sequence of a football match, as well as the corners of the goal in each image and an image of the Penn Engineering logo.

The task is to, for each image in the video sequence, compute the homography between the Penn logo and the goal, and then warp the goal points onto the ones in the Penn logo to generate a projection of the logo onto the video frame.




The below Penn logo image is being project3ed onto the goal post in the other image
![barca_real001](https://user-images.githubusercontent.com/89912646/215006627-b0117932-f536-41c4-b071-914e1c8fb946.png)
![penn_engineering_logo](https://user-images.githubusercontent.com/89912646/215006834-9aacae0f-32bf-4314-8f07-ea488334eb92.png)

The resultant final image is as shown below


![frame_0](https://user-images.githubusercontent.com/89912646/215006442-7935b4ed-d916-492b-a781-b3a66410c646.png)

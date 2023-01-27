# Virtual Billboard

## Prepare the env

We use `anaconda` (`miniconda`) to manage the python environment. Please install it before you start.

Below is a command to create a virtual environment.
```shell
conda create -n cis580_22_fall  python=3.8
```

To use this env in the current terminal 

```shell
source activate cis580_22_fall
```

Note, when working in IDE, you should select the interpreter to be this virtue environment. For example, in VSCode (after you install the python development plugins), you can press `F1` and type `select interpreter` to select the virtue environment.

Install the required pkgs:

```shell
pip install -r requirements.txt
```

Note, we already provide the VSCode debugging config in the `.vscode` folder, you can select the `Run HW1` and press `F5` to start debugging. (to select a debug configuration, press `F1` and type `Debug: select and start debugging`, once selected this config, you can directly press `F5` in the future to use the same config)

# TODO

This project utilizes the concepts of projective geometry and homographies to project an image (in this case, the Penn Engineering logo) onto a scene (a football goal) in a natural way that respects perspective.

The project includes images from a video sequence of a football match, as well as the corners of the goal in each image and an image of the Penn Engineering logo.

The task is to, for each image in the video sequence, compute the homography between the Penn logo and the goal, and then warp the goal points onto the ones in the Penn logo to generate a projection of the logo onto the video frame.

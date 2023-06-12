# SonarLocalization
ML approach to localizing in 3D space using spectrograms from sonar.

## Problem
Can we localize ourselves in an environment using bio-mimic'd bat biosonar without GNSS?

## Background
In GNSS-denied environments, localizing in a 3D environment poses difficulties. Sonar-sensing bats have the ability to 'easily' navigate their surroundings for survival (locating and hunting prey). A robotic system that bio-mimics a bat's sonar system may be able locate itself in an a-priori (previously mapped w/ sonar) environment. Zhang et. et. proved this is [possible](https://iopscience.iop.org/article/10.1088/1748-3190/acb51f/meta) using a supervised deep learning classification model, but there is a need for field testing in bat-native environments with a higher degree of GPS-accuracy to ensure robustness and applicability.

## Approach
The problem is bounded to a given geographic location (e.g. a small forest). Training data is collected and labelled with GNSS (ideally, RTK-GPS for increased accuracy). Field research is conducted by walking through an environment and triggering a series of 'echoes' (send ultrasonic sonar out) and 'listens' (recording the reflected sound coming in). At each point where an echo/listen is obtained, GNSS coordinates are logged.  
Post-processing is conducted afterwards, which includes clustering GPS coordinates using K-means into discrete local sub-regions and generating spectrograms from the sonar reflections. This serves as the training data, which is used to train a ResNet (ML classification model).  

## Training Data & Model
A given 'observation' / row of training data consists of a spectrogram (image of it). This spectrogram is fed in as an image (matrix of values). The labels (yhat) are the classified sub-regions (output of K-means on GPS coordinates).  
ResNet (need more details on what the heck this is) is trained on this data.

## Prediction
New spectrograms can be fed to the model, and a prediction of which sub-region the spectrogram came from is outputted. As the number samples are increased, the number of sub-regions can be increased to obtain finer resolution for predictions. 

# Installation & Setup
The ML code is Python, and the data is stored in MATLAB .mat files. The below setup consists of installing proper Python packages to run the. py scripts. 

## Install Python Packages
It is recommended that you use a Python virtual environment, though this is not necessary (you can ignore commands relating to virtual env below). These instructions were written for Unix systems.
0. clone this repo into a folder
1. open a new terminal
2. ```cd /path/to/where/this/repo's/code/is```
3. install virtualenv ```sudo apt install virtualenv```
4. create a new virtual environment ```virtualenv nameOfYourEnv```
5. source your virtualenv (activate it) ```source nameOfYourEnv/bin/activate```
- when you are done with the environment, deactivate the env it with ```deactivate``` and then delete it with ```rm -r nameOfYourEnv```
6. install the following python packages:
- ```pip install pandas```
- ```pip install numpy```
- ```pip install keras```
- ```pip install scipy```
- ```pip install keras_applications```
- ```pip install scikit-learn```
- ```pip install matplotlib```
- ```pip install tensorflow```

7. ensure you have the data files (allspecmic2dynFM.mat and mutliple .mat files), open the CN-Resnet152-Patch-Classification.py file, and update the file locations for variables `data1` and `data3` (should be in the first 30 lines or so).

## Running the Program
1. open new terminal
2. source (activate) your virtualenv `source nameOfYourEnv/bin/activate`
3. run the python script `python CN-Resnet152-Patch_Classification.py`

When the script runs, tensorflow will likely output a bunch of warnings (this is typical). Only be worried if there are actual errors.  
You know things are working if the model starts going through training epochs with an output similar to below:
```bash
Epoch 1/20
1/494 [..............................] - ETA: 2:40 - loss: 0.8206 - accuracy: 0.703
2/494 [..............................] - ETA: 3:10 - loss: 0.8532 - accuracy: 0.664  
  ```

### Troubleshooting
This section is dedicated to specific errors and how to fix them

#### Problem 1 -- Your Computer has a GPU and TensorFlow is failing
If you do the basic install `pip install tensorflow` and your computer has a GPU (like mine) then you will probably run into some errors. My computer outputted `Epoch 1/20` but then hit an error. To fix this, I had to disable the GPU while running the program. This is because using a GPU requires a more advanced installation of tensorflow (and other compatibility things). To disable the GPU, add this to the start of your script:
```python
import os
os.environ[CUDA_VISIBLE_DEVICES"] = "-1"
```
That fixed it for me! Note that 'fixing it' in this sense means commanding tensorflow to my CPU rather than GPU. However, a more advanced use case will find a way to install tensorflow properly to get things working with a GPU. Temp fix!

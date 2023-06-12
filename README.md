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

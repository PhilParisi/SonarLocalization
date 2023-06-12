# SonarLocalization
ML classification approach to localizing in 3D space using spectrograms from sonar

## Problem
Can we localize ourselves in an environment using bio-mimic'd bat biosonar without GNSS?

## Background
In GNSS-denied environments, localizing in a 3D environment poses difficulties. Sonar-sensing bats have the ability to 'easily' navigate their surroundings for survival (locating and hunting prey). A robotic system that bio-mimics a bat's sonar system may be able locate itself in an a-priori (previously mapped w/ sonar) environment. Zhang et. et. proved this is [possible](https://iopscience.iop.org/article/10.1088/1748-3190/acb51f/meta) but needs field testing in bat-native enviornments with a higher degree of GPS-accuracy.

## Approach
The problem is bounded to a given geographic location (e.g. a small forest). Training data is collected and labelled with GNSS (ideally, RTK-GPS for increased accuracy). Field research is conducted by walking through an environment and triggering a series of 'echoes' (send ultrasonic sonar out) and 'listens' (recording the reflected sound). At each point where an echo/listen is obtained, GPS coordinates are logged.  
Post-processing is conducted afterwards, which includes clustering GPS coordinates using K-means into discrete local regions and generating spectrograms from the sonar reflections. This serves as the training data, which is trained using a ResNet (ML classification model).  


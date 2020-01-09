# Deep-Dream
Find and Enhance Patterns in Images via Algorithmic Pareidolia

## What is Deep Dream ?

DeepDream is a computer vision program created by Google engineer Alexander Mordvintsev which uses a convolutional neural network to find and enhance patterns in images via algorithmic pareidolia, thus creating a dream-like hallucinogenic appearance in the deliberately over-processed images.

## How Deep Dream Works ?

The idea, simply, is like having a feedback loop on the image classification model. You give the model an image, and it gives you some scores for what objects it was trained on that it believes they might exist in the image. Then, you let the network to modify the input image to make these objects visible more and more. You can repeat this more than one time.

<p align="center">
<img src="https://github.com/crypto-code/Deep-Dream/blob/master/assets/model.png" height="400" align="middle" />   </p>

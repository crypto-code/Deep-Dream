# Deep-Dream
Find and Enhance Patterns in Images via Algorithmic Pareidolia

## What is Deep Dream ?

DeepDream is a computer vision program created by Google engineer Alexander Mordvintsev which uses a convolutional neural network to find and enhance patterns in images via algorithmic pareidolia, thus creating a dream-like hallucinogenic appearance in the deliberately over-processed images.

## How Deep Dream Works ?

The idea, simply, is like having a feedback loop on the image classification model. You give the model an image, and it gives you some scores for what objects it was trained on that it believes they might exist in the image. Then, you let the network to modify the input image to make these objects visible more and more. You can repeat this more than one time. Any pretrained network can be used, but in this Inception5h is used since it can accept images of different sizes.

<p align="center">
<img src="https://github.com/crypto-code/Deep-Dream/blob/master/assets/model.png" height="400" align="middle" />   </p>

Once the image is passed through the layers, a function calculates the gradient of an input image for use in the DeepDream algorithm. The gradient is then added to the input image so the mean value of the layer-tensor is increased. This process is repeated a number of times and amplifies whatever patterns the Inception model sees in the input image.

## Usage:

* The script provided runs the deep dream algorithim to create frames, and the frames are compiled into a video.
```
python dreamer.py --help

2020-01-09 21:59:38.396540: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
usage: vid_dreamer.py [-h] --input INPUT --name NAME --frames FRAMES
                      [--iter_num ITER_NUM] [--zoom ZOOM] [--rec_num REC_NUM]

Deep Dream Creator

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT        Image to use for deep dream
  --name NAME          Name of the Dream
  --frames FRAMES      Number of frames
  --iter_num ITER_NUM  Number of iterations
  --zoom ZOOM          Controls the speed of the zoom [1,2,.....]
  --rec_num REC_NUM    Number of recursive loops
```

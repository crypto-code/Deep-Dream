'''
Layer Info:
layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles
layer 6: dogs, bears, cute animals.
layer 7: faces, buildings
layer 8: fish, frogs/reptilian eyes.
layer 10: Monkies, lizards, snakes, duck
'''

from utils import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import cv2
import os
import random
from random import randint
import argparse

#-------------------------------------------------------------------------------------------------
lay_num=randint(0,10)
layer_tensor = model.layer_tensors[lay_num]

parser = argparse.ArgumentParser(description='Deep Dream Creator')
parser.add_argument('--input',type=str,required=True,help='Image to use for deep dream')
parser.add_argument('--name',type=str,required=True,help='Name of the Dream')
parser.add_argument('--frames',type=int,required=True,help='Number of frames')
parser.add_argument('--iter_num',type=int,default=10,help='Number of iterations')
parser.add_argument('--zoom',type=int,default=1,help='Controls the speed of the zoom [1,2,.....]')
parser.add_argument('--rec_num',type=int,default=0,help='Number of recursive loops')

args = parser.parse_args()

dream_name = args.name
dream_path = 'dream/{}'.format(dream_name)

if not os.path.exists(dream_path):
    os.mkdir(dream_path)

img = cv2.imread(args.input)
cv2.imwrite(dream_path+"/img_0.jpg",img)
y_size, x_size, _ = img.shape

created_count = 0
max_count = args.frames

#-------------------------------------------------------------------------------------------------
print("Layer: ", lay_num)
for i in range(0, args.frames):

    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name, i+1)):
        print('{} already exists, skipping......'.format(i+1))

    else:
        img_result = load_image(filename='dream/{}/img_{}.jpg'.format(dream_name, i))
        if i%10 is 0:
            lay_num=randint(0,10)
            layer_tensor = model.layer_tensors[lay_num]
            print("Layer: ", lay_num)

        x_trim = args.zoom
        y_trim = args.zoom
        
        img_result = img_result[0+x_trim:y_size-y_trim, 0+y_trim:x_size-x_trim]
        img_result = cv2.resize(img_result, (x_size, y_size))


        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)

        print("Iteration No: ",i+1)
        img_result = recursive_optimize(layer_tensor=layer_tensor,
                                        image=img_result,
                                        num_iterations=args.iter_num,
                                        step_size=1.0,
                                        num_repeats=args.rec_num,
                                        blend=0.2)

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)
        result = PIL.Image.fromarray(img_result, mode='RGB')
        result.save('dream/{}/img_{}.jpg'.format(dream_name, i+1))
        created_count += 1
        if created_count > max_count:
            break

#-------------------------------------------------------------------------------------------------
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('{}.avi'.format(dream_name),fourcc, 30.0, (630,870))

for i in range(int('inf')):
    if os.path.isfile('dream/{}/img_{}.jpg'.format(dream_name,i+1)):
        pass
    else:
        dream_length = i
        break

for i in range(dream_length):
    img_path = os.path.join(dream_path,'/img_{}.jpg'.format(i))
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()
#-------------------------------------------------------------------------------------------------

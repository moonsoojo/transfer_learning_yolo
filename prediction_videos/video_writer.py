#!/usr/local/bin/python3

import cv2
import argparse
import os
import natsort
import ffmpeg

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
ap.add_argument("-s", "--sequence", required=False, default='1', help="sequence to string")
args = vars(ap.parse_args())

# Arguments
dir_path = './colonoscopy-video/'
ext = args['extension']
output = args['output']
sequence = args['sequence']

images = []
dirFiles = os.listdir(dir_path)
dirFiles = natsort.natsorted(dirFiles)

for f in dirFiles:
    print(f)
    if f.endswith(ext) and f.startswith(str(sequence) + '-'):
        images.append(dir_path + f)

# Determine the width and height from the first image
image_path = os.path.join(images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20, (width, height)) # removed 'True' from the tutorial

for image in images:

    #image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))
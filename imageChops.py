# import the necessary packages
import numpy as np
from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2
from PIL import Image, ImageChops
# construct the argument parse and parse the arguments
cap = cv2.VideoCapture("birds.mp4")
frame = None
while True:
    if frame is None:
        ret, frame = cap.read()
    ret, frame2 = cap.read()
    # convert the images to grayscale
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
    fr_pil= Image.fromarray(frame)
    fr2_pil = Image.fromarray(frame2)
    diff = ImageChops.difference(fr_pil, fr2_pil)

    frame=frame2
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    im_np = np.asarray(diff)
    cv2.imshow("frame",im_np)
    cv2.waitKey(1)

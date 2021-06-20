# import the necessary packages
import numpy as np

import cv2
from PIL import Image, ImageChops

from fps import FPS


def color_changer(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # lower mask (0-10)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0 + mask1

    # set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask == 0)] = 0
    output_img = cv2.cvtColor(output_img,cv2.COLOR_BGR2RGB)
    return output_img


# construct the argument parse and parse the arguments
cap = cv2.VideoCapture("birds.mp4")
frame = None
fps=FPS()
while True:
    if frame is None:
        ret, frame = cap.read()
    ret, frame2 = cap.read()
    # convert the images to grayscale
    abc=color_changer(frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    fr_pil = Image.fromarray(frame)
    fr2_pil = Image.fromarray(frame2)

    diff = ImageChops.difference(fr_pil, fr2_pil)

    frame = frame2
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    im_np = np.asarray(diff)
    cv2.imshow("frame", im_np)
    print(fps.calc_fps())
    cv2.waitKey(1)

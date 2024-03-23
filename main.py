import sys
import os
import mss
import cv2
import numpy as np

import config
import display
import screencapture

from time import sleep


def main():
    bb = screencapture.BuffBar()
    # cv2.imshow('test', bb.ms_curr)
    # cv2.waitKey()
    for k in bb.buff_coords.keys():
        if bb.buff_coords[k]:
            cv2.imshow('test', bb.buff_imgs[k])
            cv2.waitKey()
    return


if __name__ == '__main__':
    main()

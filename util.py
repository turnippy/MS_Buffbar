import cv2
import numpy as np

import config


class ImgWrapper:
    def __init__(self, img_np=None, blank=False):
        self.isblank = blank
        self.img_np = img_np
        self.img_tk = None

    def convert_bgra_to_rgb(self):
        if not self.isblank:
            temp = np.delete(self.img_np, 3, 1)
            self.img_np = temp[..., [2, 1, 0]].copy()

    def resize_to_config(self):
        if not self.isblank:
            self.img_np = cv2.resize(self.img_np, (config.BUFF_ZOOM_DIM, config.BUFF_ZOOM_DIM))

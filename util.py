import PIL.Image
import PIL.ImageTk
import numpy as np

import config


class ImgWrapper:
    def __init__(self, img_np, blank=False):
        self.blank = blank
        self.img_np = img_np
        self.img_tk = None

    def resize_to_config(self):
        self.img_np = np.resize(self.img_np, (config.BUFF_ZOOM_DIM, config.BUFF_ZOOM_DIM))

    def convert_to_tk(self):
        self.img_tk = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.img_np))

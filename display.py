import tkinter as tk
import cv2
import config
import time

from PIL import Image, ImageTk


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ENHANCED BUFF BAR")

        self.canvas = tk.Canvas(self.root,
                                width=len(config.BUFFS_LIST)*(config.BUFF_ZOOM_DIM+40),
                                height=config.BUFF_ZOOM_DIM+40)
        self.canvas.pack(padx=20, pady=20)

        self.images = {}

    def load_images(self, imgs_in):
        """
        :param imgs_in: dcit with keys = buff name, value = np array of image
        :return: None
        """
        for item in config.BUFFS_LIST:
            self.images[item] = imgs_in[item]

    def update(self, imgs):
        """
        :param imgs: dict with keys = buff name, value = np array of image
        :return: None
        """
        self.load_images(imgs)
        self.root.after(100, self.update)


if __name__ == "__main__":
    test = Display()
    tdict = {}
    for i in config.BUFFS_LIST:
        tdict[i] = None
    test.update(tdict)
    test.root.mainloop()

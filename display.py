import tkinter as tk

import cv2
import numpy as np

import config
import util


class Display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ENHANCED BUFF BAR")

        self.images = {}

        self.canvas = tk.Canvas(self.root,
                                width=len(config.BUFFS_LIST) * (config.BUFF_ZOOM_DIM + 40),
                                height=config.BUFF_ZOOM_DIM + 40)
        self.canvas.pack(padx=20, pady=20)

    def load_images(self, imgs_in):
        """
        takes in a dict of ImgWrapper objects, upscales, and convert to PIL PhotoImage object
        :param imgs_in: dict with keys = buff name, value = np array of image
        :return: None
        """
        for item in config.BUFFS_LIST:
            imgs_in[item].resize_to_config()
            imgs_in[item].convert_to_tk()
            self.images[item] = imgs_in[item]

    def draw(self):
        """
        refreshes canvas with images from self.images
        :return: None
        """
        pad = 0
        for item in self.images:
            if not self.images[item].isblank:
                self.canvas.create_image(pad*(config.BUFF_ZOOM_DIM+20), 0,
                                         image=self.images[item].img_tk, anchor=tk.NW)
            pad += 1

    def update(self):
        """
        tkinter root update, executes every 100ms
        :return: None
        """
        if self.canvas:
            self.canvas.delete("all")
        self.draw()

        self.root.after(100, self.update)

    def run_mainloop(self):
        print("\tStarting tkinter mainloop...")
        self.root.mainloop()


if __name__ == "__main__":
    test = Display()
    tdict = {}
    for i in config.BUFFS_LIST:
        tdict[i] = util.ImgWrapper(np.array(cv2.cvtColor(cv2.imread(f"resources/{i}.png"), cv2.COLOR_BGR2RGB)))
    test.load_images(tdict)
    print("images loaded")
    test.update()
    test.run_mainloop()

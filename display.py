import pygame
from pygame.locals import *

import config
import util


class Display:
    def __init__(self):

        self.images = {}

        pygame.init()
        self.padding = 20
        self.width = len(config.BUFFS_LIST)*config.BUFF_ZOOM_DIM + (len(config.BUFFS_LIST)+1)*self.padding
        self.height = config.BUFF_ZOOM_DIM + 2*self.padding

        self.screen = pygame.display.set_mode(size=(self.width, self.height))

        self.init_screen()

        self.running = False

    def init_screen(self):
        self.screen.fill(Color('Grey'))

    def run(self):
        self.running = True
        while self.running:

            self.update()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop()

    def stop(self):
        self.running = False
        pygame.quit()

    def update(self):
        pass

    def load_process_images(self, imgs_in):
        """
        public setter for self.images
        :param imgs_in: dict with keys = buff name, value = np array of image
        :return: None
        """
        for item in config.BUFFS_LIST:
            imgs_in[item].resize_to_config()
            # imgs_in[item].convert_bgra_to_rgb()

            self.images[item] = imgs_in[item]


if __name__ == "__main__":
    test = Display()
    test.run()

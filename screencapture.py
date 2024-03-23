import os
import mss
import cv2
import numpy as np

import config

from win32gui import FindWindow, GetWindowRect


class BuffBar:
    def __init__(self):
        self.buffs = config.BUFFS_LIST

        self.ms_coords = {}
        self.buff_coords = {}
        self.buff_imgs = {}

        self.ms_curr = None

        self.update_all()

    def set_ms_coords(self):
        window_handle = FindWindow(None, "MapleStory")
        try:
            window_rect = GetWindowRect(window_handle)
        except BaseException:
            print("Window not found.")
            return
        self.ms_coords = {"left": window_rect[0], "top": window_rect[1],
                          "width": window_rect[2] - window_rect[0], "height": window_rect[3] - window_rect[1]}
        self.ms_coords["height"] = int(self.ms_coords["height"] / 2)

    def set_ms_curr(self):
        self.ms_curr = screenshot(self.ms_coords)

    def set_buff_coords(self, buff):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"resources/{buff}.png")
        templ = cv2.imread(f"{path}")
        self.set_ms_curr()
        self.buff_coords[buff] = self.calc_buff_anchor(templ)

    def calc_buff_anchor(self, template):
        """
        :param template: numpy array representing 3 channels for template
        :return: dict with keys left,top,height,width of absolute position of buff icon on screen
        matching is done with cv2.matchTemplate()
        correlation is calculated using CCOEFF_NORMED
        """
        img_gray = cv2.cvtColor(self.ms_curr, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        # look for local max (threshold > 0.60) when using CCOEFF_NORMED
        threshold = 0.6

        if len(np.where(res >= threshold)[1]) < 1:  # template not found
            return None

        loc_x = self.ms_coords["left"] + np.where(res >= threshold)[1][0]
        loc_y = self.ms_coords["top"] + np.where(res >= threshold)[0][0]

        return dict(left=loc_x, top=loc_y, width=template.shape[1],
                    height=template.shape[0])

    def update_all(self):
        self.set_ms_coords()
        for item in self.buffs:
            self.set_buff_coords(item)
            if self.buff_coords[item]:
                self.buff_imgs[item] = screenshot(self.buff_coords[item])
            else:
                self.buff_imgs[item] = None


def screenshot(rect):
    """
    :param rect: dict with keys left,top,height,width corresponding to absolute position on screen
    :return: np array representing 3 channels of image
    """
    with mss.mss() as sct:
        return np.array(sct.grab(rect))

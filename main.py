import threading

from time import sleep

import display
import screencapture


class App:
    def __init__(self):
        self.sc = screencapture.ScreenCap()
        self.disp = display.Display()

        self.thread_active = False
        self.thread = threading.Thread(target=self.get_and_load_imgs, daemon=True)

    def get_and_load_imgs(self):
        # passes images from screencapture obj to display obj
        while self.thread_active:
            self.d.load_process_images(self.bb.buff_imgs)
            sleep(0.2)

    def run(self):
        print("\tStarting app thread...")
        self.thread_active = True
        self.thread.start()

    def stop(self):
        print("\tStopping app thread...")
        self.thread_active = False


def main():
    a = App()
    a.sc.run()
    a.disp.run()
    sleep(10)
    a.sc.stop()
    a.disp.stop()


if __name__ == '__main__':
    main()

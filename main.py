import threading

from time import sleep

import display
import screencapture


class App:
    def __init__(self):
        self.bb = screencapture.BuffBar()
        self.d = display.Display()

        self.thread_active = False
        self.thread = threading.Thread(target=self.get_and_load_imgs, daemon=True)

    def get_and_load_imgs(self):
        while self.thread_active:
            self.d.load_process_images(self.bb.buff_imgs)
            sleep(0.1)

    def run(self):
        print("\tStarting app thread...")
        self.thread_active = True
        self.thread.start()

    def stop(self):
        print("\tStopping app thread...")
        self.thread_active = False


def main():
    a = App()
    a.bb.run()
    a.run()
    a.d.update()
    a.d.run_mainloop()
    a.bb.stop()
    a.stop()


if __name__ == '__main__':
    main()

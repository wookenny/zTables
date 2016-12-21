#!/usr/bin/env python
"""
    Arbalet - ARduino-BAsed LEd Table
    Image reader

    Reads an animated image and render it

    Copyright 2015 Yoan Mollard - Arbalet project - http://github.com/arbalet-project
    License: GPL version 3 http://www.gnu.org/licenses/gpl.html
"""
from PIL import Image
from os.path import isfile
from arbalet.core import Application
from time import sleep
import argparse, pygame

class ImageReader(Application):
    def __init__(self, argparser):
        Application.__init__(self, argparser)
        self.image = None
        self.palette = None
        self.vertical = False
        self.quit     = False

    def process_events(self):
        for event in self.arbalet.events.get():
            # Keyboard control
            if event.type in [pygame.KEYDOWN, pygame.KEYUP, pygame.JOYBUTTONDOWN, pygame.JOYHATMOTION]:
                self.quit = True

    def play_file(self, f):
        if isfile(f):
            self.image = Image.open(f)
            if self.image.size[0]<self.image.size[1]:
                self.vertical = True
            while not self.quit:
                self.process_events()
                try:
                    self.update_model(self.image.convert('RGB').resize((self.width, self.height) if self.vertical
                                                                       else (self.height, self.width)))
                    self.image.seek(self.image.tell()+1)
                except EOFError:
                    if self.args.loop:
                        self.image.seek(0)
                    else:
                        return
                sleep(self.image.info['duration']/1000.)  # Gif duration are in msec
        else:
            raise IOError('No such file or directory: \'{}\''.format(f))

    def update_model(self, image):
        with self.model:
            for h in range(self.height):
                for w in range(self.width):
                    pixel = image.getpixel((w, h) if self.vertical else (h, w))
                    self.model.set_pixel(h, w, pixel)

    def run(self):
        self.play_file(self.args.input)



parser = argparse.ArgumentParser(description='Render an animated image (gif, apng, mng...) on Arbalet')
image = 'gifs/mario.jumping.black.gif' #USE random image
parser.add_argument('-i', '--input',
                    action='store_const',
                    const=True,
                    default = image,
                    help='Path to the image(s) to render')

parser.add_argument('-l', '--loop',
                    action='store_const',
                    const=True,
                    default=True,
                    help='Keep playing infinitely')

parser.add_argument('-do', '--display-original',
                    action='store_const',
                    const=True,
                    default=False,
                    help='Display the original image (require access to X display)')

ImageReader(parser).start()

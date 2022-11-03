from pico2d import *

class Grass:
    def __init__(self, height):
        self.image = load_image('grass.png')
        self.h = height

    def draw(self):
        self.image.draw(400, self.h)

    def update(self): pass

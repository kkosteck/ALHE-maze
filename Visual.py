import time
import math
import pygame, sys
from pygame.locals import *


LIGHT_GRAY=(224,224,224)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

WIDTH=800
HEIGHT=800


class Visual:
    def __init__(self, n, m, title="maze"):
        self.n= HEIGHT / n
        self.m= WIDTH / m
        if self.m < self.n:
            self.n = self.m
        self.padding = (HEIGHT - self.n*n) / 2
        self.display=pygame.display.set_mode((WIDTH,HEIGHT))
        self.display.fill(LIGHT_GRAY)
        pygame.display.set_caption(title)


    def draw_cell(self, x, y, color=LIGHT_GRAY, delay=0,update=True):
        x = x*self.m
        y = self.padding+(y*self.n)
        w = self.m
        h = self.n
        if not w.is_integer():
            w = math.ceil(w)
        if not h.is_integer():
            h = math.ceil(h)
        pygame.draw.rect(self.display, color, pygame.Rect(x, y, w, h))
        if update:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

        time.sleep(delay)

    def draw_maze(self, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    self.draw_cell(j,i,BLACK, 0, False)

    def show(self, data):
        self.display.fill(LIGHT_GRAY)
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    self.draw_cell(j,i,BLACK, 0, False)
                elif data[i][j] == 2:
                    self.draw_cell(j,i,GREEN, 0, False)
                elif data[i][j] == 3:
                    self.draw_cell(j,i,RED, 0, False)
                elif data[i][j] == 4:
                    self.draw_cell(j,i,BLUE, 0, False)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            keys=pygame.key.get_pressed()
            if keys[K_SPACE]:
                break
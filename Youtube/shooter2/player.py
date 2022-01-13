import pygame

class Player():
    def __init__(self, window):
        self.x = 300
        self.y = 300
        self.color = (255, 0, 0)
        self.window = window
        self.size = 30

    def show(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

    def move(self):
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= .5
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += .5

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

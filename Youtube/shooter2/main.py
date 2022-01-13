import pygame, sys
from player import Player

window = pygame.display.set_mode((600, 600))

running = True
player = Player(window)

while running:
    window.fill((0, 0, 0))
    player.show()
    player.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
    pygame.display.update()

# Example file showing a basic pygame "game loop"
import pygame
import math
import os

from utils import Vector2
from dialog_box import DialogBox


# pygame setup
pygame.init()

window_w = 800
window_h = 800

screen  = pygame.display.set_mode((window_w, window_h))
clock   = pygame.time.Clock()
running = True
delta_time = 1

dialog_box = DialogBox(Vector2(0.0, 0.0), "hello world", 20, 10)
print("bonjour")
dialog_box.load_text_textures()

while running:
    screen.fill("black")

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dialog_box.draw_dialog_box(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    delta_time = clock.tick(120)  # limits FPS to 120
    delta_time /= 1000.0
 

pygame.quit()
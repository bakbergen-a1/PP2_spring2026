import pygame
import sys
from datetime import datetime
from clock import draw_clock_hands

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

# load background image
background = pygame.image.load("practice9/mickeys_clock/images/mickeyclock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw clock image
    screen.blit(background, (0, 0))

    # get current system time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # draw hands
    draw_clock_hands(screen, WIDTH // 2, HEIGHT // 2, minutes, seconds)

    pygame.display.flip()

    # update every second
    fps_clock.tick(1)
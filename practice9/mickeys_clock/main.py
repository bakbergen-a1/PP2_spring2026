import pygame
import sys
from datetime import datetime
from clock import draw_clock_hands

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real Mickey Clock")

# full image outside as real wall clock
background = pygame.image.load("practice9/mickeys_clock/images/mickeyclock.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

fps_clock = pygame.time.Clock()

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # show full photo
    screen.blit(background, (0, 0))

    # real system time
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # draw real clock hands
    draw_clock_hands(screen, CENTER_X, CENTER_Y, hour, minute, second)

    pygame.display.flip()
    fps_clock.tick(1)
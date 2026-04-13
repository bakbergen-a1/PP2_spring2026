import pygame
import math


def draw_hand(screen, x, y, length, angle, color, width):
    radians = math.radians(angle - 90)

    end_x = x + length * math.cos(radians)
    end_y = y + length * math.sin(radians)

    pygame.draw.line(screen, color, (x, y), (end_x, end_y), width)


def draw_clock_hands(screen, x, y, hour, minute, second):
    # real angles
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    second_angle = second * 6

    # hour hand
    draw_hand(screen, x, y, 90, hour_angle, (0, 0, 0), 10)

    # minute hand
    draw_hand(screen, x, y, 130, minute_angle, (0, 0, 255), 6)

    # second hand
    draw_hand(screen, x, y, 160, second_angle, (255, 0, 0), 3)

    # center point
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 8)
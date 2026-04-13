import pygame
import math


def draw_hand(screen, center_x, center_y, length, angle, color, width):
    """
    Draw one clock hand
    """
    radians = math.radians(angle - 90)

    end_x = center_x + length * math.cos(radians)
    end_y = center_y + length * math.sin(radians)

    pygame.draw.line(
        screen,
        color,
        (center_x, center_y),
        (end_x, end_y),
        width
    )


def draw_clock_hands(screen, x, y, minutes, seconds):
    """
    Draw minute and second hands
    """
    # 360 / 60 = 6 degrees each
    minute_angle = minutes * 6
    second_angle = seconds * 6

    # right hand = minute hand
    draw_hand(screen, x, y, 120, minute_angle, (0, 0, 0), 8)

    # left hand = second hand
    draw_hand(screen, x, y, 160, second_angle, (255, 0, 0), 4)

    # center dot
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 8)
import pygame
from collections import deque

def flood_fill(surface, start_pos, fill_color):
    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)

    if target_color == fill_color:
        return

    queue = deque([start_pos])

    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        current_color = surface.get_at((x, y))
        if current_color != target_color:
            continue

        surface.set_at((x, y), fill_color)

        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))


def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_circle(surface, color, center, radius, size, fill=False):
    if fill:
        pygame.draw.circle(surface, color, center, radius)
    else:
        pygame.draw.circle(surface, color, center, radius, size)


def draw_rect(surface, color, start, end, size, fill=False):
    rect = pygame.Rect(start[0], start[1],
                       end[0] - start[0], end[1] - start[1])
    if fill:
        pygame.draw.rect(surface, color, rect)
    else:
        pygame.draw.rect(surface, color, rect, size)
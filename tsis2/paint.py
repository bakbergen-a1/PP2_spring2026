import pygame
import sys
import os
from datetime import datetime
from tools import flood_fill, draw_line, draw_rect, draw_circle

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint App")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

color = BLACK

# Tools
tool = "pencil"
brush_size = 2

drawing = False
start_pos = None
last_pos = None

# Text tool
text_active = False
text_pos = None
text_input = ""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_canvas(canvas):
    folder = os.path.join(BASE_DIR, "assets")

    
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = datetime.now().strftime("canvas_%Y%m%d_%H%M%S.png")
    path = os.path.join(folder, filename)

    pygame.image.save(canvas, path)
    print("Saved:", path)

def draw_ui():
    text = font.render(f"Tool: {tool} | Brush: {brush_size}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

running = True
while running:
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))
    draw_ui()

    if tool == "line" and drawing and start_pos:
        pygame.draw.line(screen, color, start_pos, pygame.mouse.get_pos(), brush_size)

    if tool == "text" and text_active:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard shortcuts
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas(canvas)

            # Text tool typing
            if text_active:
                if event.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    canvas.blit(img, text_pos)
                    text_active = False
                    text_input = ""

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_input = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

            # Tool switching (simple)
            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tool == "fill":
                flood_fill(canvas, event.pos, color)

            elif tool == "text":
                text_active = True
                text_pos = event.pos
                text_input = ""

            else:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                if tool == "pencil":
                    pygame.draw.line(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "line":
                    draw_line(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "rect":
                    draw_rect(canvas, color, start_pos, end_pos, brush_size)

                elif tool == "circle":
                    radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                    draw_circle(canvas, color, start_pos, radius, brush_size)

            drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
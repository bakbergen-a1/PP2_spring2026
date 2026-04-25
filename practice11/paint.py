import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# Current drawing color
color = (255, 0, 0)

# Current drawing mode
mode = "square"  # initial mode

drawing = False
start_pos = None

# Fill background with black
screen.fill((0, 0, 0))

running = True
while running:
    for event in pygame.event.get():

        # Exit the program
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # SHAPES / MODES
            if event.key == pygame.K_s:
                mode = "square"
            if event.key == pygame.K_t:
                mode = "triangle"
            if event.key == pygame.K_e:
                mode = "equilateral"
            if event.key == pygame.K_r:
                mode = "rhombus"
            if event.key == pygame.K_x:
                mode = "eraser"

            # COLORS
            if event.key == pygame.K_1:
                color = (255, 0, 0)  # red
            if event.key == pygame.K_2:
                color = (0, 255, 0)  # green
            if event.key == pygame.K_3:
                color = (0, 0, 255)  # blue
            if event.key == pygame.K_4:
                color = (255, 255, 0)  # yellow
            if event.key == pygame.K_5:
                color = (255, 255, 255)  # white

        # Mouse press starts drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Mouse release finishes drawing shape
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # SQUARE
            if mode == "square":
                size = min(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(screen, color, (*start_pos, size, size))

            # RIGHT TRIANGLE
            elif mode == "triangle":
                points = [start_pos, (end_pos[0], start_pos[1]), end_pos]
                pygame.draw.polygon(screen, color, points)

            # EQUILATERAL TRIANGLE
            elif mode == "equilateral":
                x, y = start_pos
                size = abs(end_pos[0] - start_pos[0])
                points = [(x, y), (x + size, y), (x + size//2, y - size)]
                pygame.draw.polygon(screen, color, points)

            # RHOMBUS
            elif mode == "rhombus":
                x1, y1 = start_pos
                x2, y2 = end_pos
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                pygame.draw.polygon(screen, color, points)

    # ERASER TOOL (draws black circles while dragging)
    if drawing and mode == "eraser":
        pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 15)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
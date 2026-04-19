import pygame

pygame.init()

# Window size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# Current drawing color (default: red)
color = (255, 0, 0)

# Drawing mode: "rect", "circle", "eraser"
mode = "rect"

drawing = False
start_pos = None

# Fill background (used for erasing)
screen.fill((0, 0, 0))

running = True
while running:
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # 🎮 Keyboard controls
        if event.type == pygame.KEYDOWN:

            # Switch drawing modes
            if event.key == pygame.K_r:
                mode = "rect"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_e:
                mode = "eraser"

            # 🎨 Change colors
            if event.key == pygame.K_1:
                color = (255, 0, 0)   # red
            if event.key == pygame.K_2:
                color = (0, 255, 0)   # green
            if event.key == pygame.K_3:
                color = (0, 0, 255)   # blue
            if event.key == pygame.K_4:
                color = (255, 255, 0) # yellow
            if event.key == pygame.K_5:
                color = (255, 255, 255) # white

        # 🖱 Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # 🖱 Mouse button released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            # Draw rectangle
            if mode == "rect":
                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]
                pygame.draw.rect(screen, color, (x, y, width, height))

            # Draw circle
            elif mode == "circle":
                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]
                radius = int((dx*2 + dy*2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius)

    # Eraser (draws while mouse is held down)
    if drawing and mode == "eraser":
        pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 15)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
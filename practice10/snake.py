import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Snake body (list of segments)
snake = [(100,100)]

# Initial movement direction
direction = (20, 0)

# Initial food position
food = (200,200)

# Score, level and speed
score = 0
level = 1
speed = 5

font = pygame.font.SysFont(None, 30)

# Function to generate food NOT on snake
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, 20)
        y = random.randrange(0, HEIGHT, 20)
        if (x,y) not in snake:
            return (x,y)

running = True
while running:
    # Fill background (black)
    screen.fill((0,0,0))

    # Handle window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    # Move snake (new head position)
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("Game Over")
        running = False

    # Check collision with itself
    if head in snake:
        print("Game Over")
        running = False

    # Add new head
    snake.insert(0, head)

    # Check if snake eats food
    if head == food:
        score += 1
        food = generate_food()

        # Increase level and speed every 3 points
        if score % 3 == 0:
            level += 1
            speed += 1
    else:
        # Remove last segment (move forward)
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0,255,0), (*segment,20,20))

    # Draw food
    pygame.draw.rect(screen, (255,0,0), (*food,20,20))

    # Draw score and level
    text = font.render(f"Score: {score} Level: {level}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
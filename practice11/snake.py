import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100,100)]
direction = (20, 0)

score = 0
level = 1
speed = 5

font = pygame.font.SysFont(None, 30)

def generate_food():
    while True:
        x = random.randrange(0, WIDTH, 20)
        y = random.randrange(0, HEIGHT, 20)
        if (x,y) not in snake:
            value = random.choice([1,2,3])
            return (x,y), value

(food, food_value) = generate_food()
food_timer = 0

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        print("Game Over")
        running = False

    if head in snake:
        print("Game Over")
        running = False

    snake.insert(0, head)

    food_timer += 1

    if head == food:
        score += food_value
        (food, food_value) = generate_food()
        food_timer = 0

        if score % 3 == 0:
            level += 1
            speed += 1
    else:
        snake.pop()

    if food_timer > 100:
        (food, food_value) = generate_food()
        food_timer = 0

    for segment in snake:
        pygame.draw.rect(screen, (0,255,0), (*segment,20,20))

    if food_value == 1:
        color = (255,0,0)
    elif food_value == 2:
        color = (0,0,255)
    else:
        color = (255,255,0)

    pygame.draw.rect(screen, color, (*food,20,20))

    text = font.render(f"Score: {score} Level: {level}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
import pygame
import random
import json

from persistence import save_score, load_leaderboard

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(220, 600, 50, 100)

cars = []
powerups = []

score = 0
distance = 0
speed = 5

power = None
power_timer = 0

game_over = False


def spawn_car():
    if random.random() < 0.03:
        x = random.choice([100, 220, 340])
        cars.append(pygame.Rect(x, -100, 50, 100))


def spawn_power():
    if random.random() < 0.01:
        x = random.choice([100, 220, 340])
        typ = random.choice(["nitro", "shield", "repair"])
        powerups.append([pygame.Rect(x, -50, 40, 40), typ])


running = True

while running:
    screen.fill((40, 40, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_LEFT]:
            player.x -= 5
        if keys[pygame.K_RIGHT]:
            player.x += 5

        spawn_car()
        spawn_power()

        # cars movement
        for car in cars:
            car.y += speed
            if player.colliderect(car):
                if power == "shield":
                    power = None
                    cars.remove(car)
                else:
                    game_over = True

        # powerups
        for p in powerups:
            rect, typ = p
            rect.y += 5

            if player.colliderect(rect):
                power = typ
                power_timer = 180
                powerups.remove(p)

        # power timer
        if power_timer > 0:
            power_timer -= 1
        else:
            power = None

        current_speed = speed * 2 if power == "nitro" else speed

        distance += current_speed
        score += 1

    pygame.draw.rect(screen, (0, 255, 0), player)

    for car in cars:
        pygame.draw.rect(screen, (255, 0, 0), car)

    for p in powerups:
        rect, typ = p
        color = (255, 255, 0) if typ == "nitro" else (0, 0, 255)
        pygame.draw.rect(screen, color, rect)

    font = pygame.font.SysFont(None, 30)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"Distance: {distance}", True, (255,255,255)), (10,40))

    if power:
        screen.blit(font.render(f"Power: {power}", True, (255,255,0)), (10,70))

    if game_over:
        screen.blit(font.render("GAME OVER - press R", True, (255,0,0)), (120,300))

        save_score(score, distance)

        if keys[pygame.K_r]:
            cars.clear()
            powerups.clear()
            score = 0
            distance = 0
            power = None
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
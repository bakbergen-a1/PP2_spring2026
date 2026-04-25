import pygame
import random

pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Player
player = pygame.Rect(180, 500, 40, 60)

# Enemy (NEW)
enemy = pygame.Rect(random.randint(50, WIDTH - 50), -60, 40, 60)
enemy_speed = 5

# Coins
coins = []
coin_count = 0

def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    coin = pygame.Rect(x, -20, 20, 20)
    coins.append(coin)

running = True
spawn_timer = 0

while running:
    screen.fill((30, 30, 30))

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Spawn coins
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_coin()
        spawn_timer = 0

    # Move coins
    for coin in coins[:]:
        coin.y += 5
        pygame.draw.rect(screen, (255, 215, 0), coin)

        if player.colliderect(coin):
            coins.remove(coin)
            coin_count += 1

        elif coin.y > HEIGHT:
            coins.remove(coin)

    # Move enemy
    enemy.y += enemy_speed

    # Respawn enemy
    if enemy.y > HEIGHT:
        enemy.x = random.randint(50, WIDTH - 50)
        enemy.y = -60

    # Collision with player
    if player.colliderect(enemy):
        print("Game Over")
        running = False

    # Increase enemy speed every 10 coins
    if coin_count != 0 and coin_count % 10 == 0:
        enemy_speed += 0.02

    # Draw enemy
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Draw coin counter
    text = font.render(f"Coins: {coin_count}", True, (255,255,255))
    screen.blit(text, (WIDTH - 120, 10))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
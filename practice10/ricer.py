import pygame
import random

pygame.init()

# Screen size
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# Player car (rectangle)
player = pygame.Rect(180, 500, 40, 60)

# Coins list and counter
coins = []
coin_count = 0

# Function to spawn a coin at random x position
def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    coin = pygame.Rect(x, -20, 20, 20)
    coins.append(coin)

running = True
spawn_timer = 0

while running:
    # Fill background (dark gray)
    screen.fill((30, 30, 30))

    # Player movement using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Spawn coins every few frames
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_coin()
        spawn_timer = 0

    # Move and draw coins
    for coin in coins[:]:
        coin.y += 5
        pygame.draw.rect(screen, (255, 215, 0), coin)  # gold color

        # Check collision with player (collect coin)
        if player.colliderect(coin):
            coins.remove(coin)
            coin_count += 1

        # Remove coin if it goes off screen
        elif coin.y > HEIGHT:
            coins.remove(coin)

    # Draw player car
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Draw coin counter (top right)
    text = font.render(f"Coins: {coin_count}", True, (255,255,255))
    screen.blit(text, (WIDTH - 120, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)
import pygame
import random

class Game:
    def __init__(self):
        self.reset()

        # load image 
        self.player_img = pygame.image.load("tsis3/assets/player.png")
        self.player_img = pygame.transform.scale(self.player_img, (40, 80))  
        self.enemy_img = pygame.image.load("tsis3/assets/enemy.png")
        self.enemy_img = pygame.transform.scale(self.enemy_img, (40, 80)) 

        self.coin_img = pygame.image.load("tsis3/assets/coin.png")
        self.coin_img = pygame.transform.scale(self.coin_img, (20, 20)) 
        # 🔊 звуки
        self.coin_sound = pygame.mixer.Sound("tsis3/assets/coin.wav")
        self.crash_sound = pygame.mixer.Sound("tsis3/assets/crash.wav")

    def reset(self):
        self.player = pygame.Rect(220, 600, 40, 80)  
        self.enemies = []
        self.coins = []

        self.score = 0
        self.distance = 0
        self.speed = 5

        self.game_over = False

    def spawn_enemy(self):
        if random.random() < 0.03:
            x = random.choice([100, 220, 340])
            self.enemies.append(pygame.Rect(x, -80, 40, 80))  

    def spawn_coin(self):
        if random.random() < 0.02:
            x = random.choice([100, 220, 340])
            self.coins.append(pygame.Rect(x, -20, 20, 20))  

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5

        self.spawn_enemy()
        self.spawn_coin()

        # enemy
        for enemy in self.enemies:
            enemy.y += self.speed

            if self.player.colliderect(enemy):
                self.crash_sound.play()
                self.game_over = True

        # coins
        for coin in self.coins:
            coin.y += self.speed

            if self.player.colliderect(coin):
                self.coin_sound.play()
                self.score += 10
                self.coins.remove(coin)

        self.distance += self.speed
        self.score += 1

    def draw(self, screen):
        # player
        screen.blit(self.player_img, (self.player.x, self.player.y))

        # enemy
        for enemy in self.enemies:
            screen.blit(self.enemy_img, (enemy.x, enemy.y))

        # coins
        for coin in self.coins:
            screen.blit(self.coin_img, (coin.x, coin.y))

        # text
        font = pygame.font.SysFont(None, 30)
        screen.blit(font.render(f"Score: {self.score}", True, (255,255,255)), (10,10))
        screen.blit(font.render(f"Distance: {self.distance}", True, (255,255,255)), (10,40))
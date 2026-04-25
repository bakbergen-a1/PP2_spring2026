import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "play"

    def draw(self):
        font = pygame.font.SysFont(None, 60)
        small = pygame.font.SysFont(None, 30)

        self.screen.blit(font.render("RACER GAME", True, (255,255,255)), (120,250))
        self.screen.blit(small.render("Press ENTER", True, (200,200,200)), (160,350))


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.distance = 0

    def set_data(self, score, distance):
        self.score = score
        self.distance = distance

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return "retry"
            if event.key == pygame.K_m:
                return "menu"

    def draw(self):
        font = pygame.font.SysFont(None, 50)
        small = pygame.font.SysFont(None, 30)

        self.screen.blit(font.render("GAME OVER", True, (255,0,0)), (120,250))
        self.screen.blit(small.render(f"Score: {self.score}", True, (255,255,255)), (160,320))
        self.screen.blit(small.render("R - retry, M - menu", True, (200,200,200)), (130,400))


class LeaderboardScreen:
    def __init__(self, screen, data):
        self.screen = screen
        self.data = data

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "back"

    def draw(self):
        self.screen.fill((30,30,30))

        font = pygame.font.SysFont(None, 40)
        small = pygame.font.SysFont(None, 30)

        self.screen.blit(font.render("LEADERBOARD", True, (255,255,255)), (120,80))

        y = 150
        for i, d in enumerate(self.data[:10]):
            text = small.render(f"{i+1}. {d['name']} - {d['score']}", True, (255,255,255))
            self.screen.blit(text, (120,y))
            y += 30
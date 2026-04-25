import pygame
from racer import Game
from ui import MainMenu, GameOverScreen, LeaderboardScreen
from persistence import save_score, load_leaderboard

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game = Game()

menu = MainMenu(screen)
game_over = GameOverScreen(screen)
leaderboard = LeaderboardScreen(screen, load_leaderboard())

state = "menu"
player_name = "Player"

running = True

while running:
    screen.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            action = menu.handle_event(event)
            if action == "play":
                game.reset()
                state = "game"

        elif state == "game_over":
            action = game_over.handle_event(event)
            if action == "retry":
                game.reset()
                state = "game"
            elif action == "menu":
                state = "menu"

        elif state == "leaderboard":
            action = leaderboard.handle_event(event)
            if action == "back":
                state = "menu"

    if state == "menu":
        menu.draw()

    elif state == "game":
        game.update()
        game.draw(screen)

        if game.game_over:
            save_score(player_name, game.score, game.distance)
            game_over.set_data(game.score, game.distance)
            state = "game_over"

    elif state == "game_over":
        game_over.draw()

    elif state == "leaderboard":
        leaderboard.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

playlist = ["practice9/music_player/music/music_1.mp3", "practice9/music_player/music/music_2.mp3"]
player = MusicPlayer(playlist)

while True:
    screen.fill((255, 255, 255))

    text = font.render(f"Track: {player.current_track_name()}", True, (0, 0, 0))
    screen.blit(text, (20, 80))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
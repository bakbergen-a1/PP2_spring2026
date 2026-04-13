import pygame
import os

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def play(self):
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def current_track_name(self):
        return os.path.basename(self.playlist[self.index])
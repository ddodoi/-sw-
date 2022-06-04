import pygame


class Bgm():

    def __init__(self, file):
        pygame.mixer.init()
        self.set_volume(0.2)
        self.set_music(file)

    def set_music(self, file):
        self.file = file

    def play_music(self):
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume)

    def set_volume(self, volume):
        self.volume = volume

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()


if __name__ == '__main__':
    print('This is sound module')

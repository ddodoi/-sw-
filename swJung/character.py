import pygame
import os


class Character:
    def __init__(self, size, screen, Path):
        self.x, self.y = 240, 765
        self.age = 1
        self.size = size
        self.screen = screen
        self.Path = Path
        self.put_img(os.path.join(self.Path, 'img',
                     f'{self.age}_left_front_img.png'))
        self.change_size(120, 120)  # 초기 캐릭터 크기 설정
        self.init_position()  # 초기 위치

    def put_img(self, address):
        if address[-3:] == "png":  # png 확장자에 대한 설정
            self.img = pygame.image.load(address).convert_alpha()
            self.sx, self.sy = self.img.get_size()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def init_position(self):  # 초기위치 설정
        self.x = 240
        self.y = 765
        # size[1]-self.sy-15

    def flip(self):
        self.img = pygame.transform.flip(
            self.img, True, False)
        self.show(self.screen)

    def walk(self, walkcount, turn, stop, walkcount_max):  # 걷는 모션
        walk_speed = walkcount_max // 4
        if walkcount == walkcount_max:
            walkcount = 0

        if not stop:
            self.put_img(os.path.join(self.Path, 'img',
                         f'{self.age}_walking_motion{(walkcount // walk_speed)+1}.png'))
            self.change_size(120, 120)
            if not turn:
                self.flip()
            walkcount += 1
        if stop:
            self.put_img(os.path.join(self.Path, 'img',
                         f'{self.age}_walking_motion4.png'))
            self.change_size(120, 120)
            walkcount = 0
            if not turn:
                self.flip()
        return walkcount

    def set_position(self, x, y):
        self.x, self.y = x, y

    def stage_chage(self):
        self.age += 1
        if self.age > 4:
            self.age = 1
        self.put_img(os.path.join(self.Path, 'img',
                     f'{self.age}_left_front_img.png'))
        self.change_size(120, 120)
        self.init_position()


if __name__ == '__main__':
    print('This is character module')

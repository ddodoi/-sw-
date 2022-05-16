import pygame


class Character:
    def __init__(self, size, screen):
        self.x = self.y = self.move = 0
        self.age = 1
        self.size = size
        self.screen = screen
        self.put_img('./img/1_left_front_img.png')
        self.change_size(120, 120)  # 초기 캐릭터 크기 설정
        self.init_position(self.size)  # 초기 위치

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

    def init_position(self, size):  # 초기위치 설정
        self.x = round(size[0]/2-self.sx/2)
        self.y = size[1]-self.sy-15

    def flip(self):
        self.img = pygame.transform.flip(
            self.img, True, False)
        self.show(self.screen)

    def set_position(self, x, y):
        self.x, self.y = x, y

    def stage_chage(self):
        self.age += 1
        if self.age > 4:  # 추후수정
            self.age = 1
        self.put_img(f'./img/{self.age}_left_front_img.png')
        self.change_size(120, 120)
        self.init_position(self.size)


if __name__ == '__main__':
    print('This is character module')

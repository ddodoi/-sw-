import pygame

# 게임초기화
pygame.init()

# 게임창 옵션 설정
size = [600, 900]
screen = pygame.display.set_mode(size)
title = 'My Game'
pygame.display.set_caption(title)

# 게임 내 필요한 설정
clock = pygame.time.Clock()  # 시간 변수 설정
black = (0, 0, 0)
white = (255, 255, 255)
color = black     # 색상설정 RGB


class char:
    def __init__(self):
        self.x = self.y = self.move = 0

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

    def show(self):
        screen.blit(self.img, (self.x, self.y))


ch = char()
ch.put_img('./img/1st_left_front_img.png')
ch.change_size(120, 120)  # 초기 캐릭터 크기 설정
ch.x = round(size[0]/2-ch.sx/2)  # 초기 위치
ch.y = size[1]-ch.sy-15
ch.move = 5  # 이동량

left_go = right_go = down_go = up_go = False

# main event
Running = True
while Running:
    # FPS 설정
    clock.tick(60)  # while문 반복 1초에 60번 간격으로 설정

    # 입력감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit에 대한 명령일 경우 종료
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False

    # 입력, 시간에 따른변화
    if left_go:
        ch.x -= ch.move
        if ch.x <= 0:
            ch.x = 0
    elif right_go:
        ch.x += ch.move
        if ch.x >= size[0]-ch.sx:
            ch.x = size[0]-ch.sx
    elif up_go:
        ch.y -= ch.move
        if ch.y <= 0:
            ch.y = 0
    elif down_go:
        ch.y += ch.move
        if ch.y >= size[1]-ch.sy-15:
            ch.y = size[1]-ch.sy-15
    print(event)
    # 그리기
    screen.fill(color)
    ch.show()
    # 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()

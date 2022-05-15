import pygame
import time
from character import Character  # 캐릭터 모듈 import
#from envrionment import Env
DEBUGGING = True  # 디버깅 모드 변수
# 게임초기화
pygame.init()

# 게임창 옵션 설정
background_size = [600, 900]  # 화면크기
screen = pygame.display.set_mode(background_size)  # 화면크기 세팅
title = 'My Game'
pygame.display.set_caption(title)  # 제목세팅
walk_sound = pygame.mixer.Sound(  # 소리세팅
    './sound/walksound.mp3')
door_sound = pygame.mixer.Sound(
    './sound/doorsound.mp3'
)
# 게임 내 필요한 설정
clock = pygame.time.Clock()  # 시간 변수 설정
black = (0, 0, 0)
white = (255, 255, 255)
color = black     # 색상설정 RGB
stage = 0
stage_name = ['<소년기>', '<청년기>',
              '<장년기>', '<노년기>']
choices = [('Study', 'Art'),
           ('Major', 'Love'),
           ('Work', 'Family')]  # 선택지
select = []  # 선택지 저장
ch = Character(background_size)  # 캐릭터 객체 설정
# env = Env()  # 게임 환경 객체 설정


def door_dist(x, y):
    if y == 375 and 295 <= x <= 370:
        return 'Right'
    elif y == 375 and 100 <= x <= 175:
        return 'Left'


left_go = right_go = down_go = up_go = False  # 키 입력 변수

movement = 5  # 이동량

# main event
Running = True  # 게임 진행 변수
while Running:
    # FPS 설정
    clock.tick(60)  # while문 반복 1초에 60번 간격으로 설정
    try:
        background = pygame.image.load(f'./img/Room{stage+1}_final_cg.png')
    except FileNotFoundError:
        break
    # 입력감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit에 대한 명령일 경우 종료
            Running = False
        if event.type == pygame.KEYDOWN:  # key를 눌렀을때
            walk_sound.play(-1)  # 걷는소리 재생
            time.sleep(0.1)  # 소리 재생 딜레이 방지용 0.1초 움직임 딜레이
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif door_dist(ch.x, ch.y) == 'Left' and pygame.K_SPACE:
                door_sound.play()
                select.append(choices[stage][0])
                ch.stage_chage()
                stage += 1
            elif door_dist(ch.x, ch.y) == 'Right' and pygame.K_SPACE:
                door_sound.play()
                select.append(choices[stage][1])
                ch.stage_chage()
                stage += 1

        elif event.type == pygame.KEYUP:  # key를 뗐을때
            walk_sound.fadeout(450)  # 0.45초 딜레이후 걷는 소리 재생 종료
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
        ch.x -= movement
        if ch.x <= 0:
            ch.x = 0
    elif right_go:
        ch.x += movement
        if ch.x >= background_size[0]-ch.sx:
            ch.x = background_size[0]-ch.sx
    elif up_go:
        ch.y -= movement
        if ch.y <= 375:
            ch.y = 375
    elif down_go:
        ch.y += movement
        if ch.y >= background_size[1]-ch.sy-15:
            ch.y = background_size[1]-ch.sy-15
    if DEBUGGING:  # 캐릭터 좌표 디버깅
        print(ch.x, ch.y)
        print(select)
    # 그리기
    screen.fill(color)
    screen.blit(background, (0, 0))
    ch.show(screen)  # 캐릭터를 스크린에 표시
    # 폰트설정
    font = pygame.font.Font('./font/DungGeunMo.ttf', 20)
    # 폰트를 이미지로 변경
    text = font.render(f'{stage_name[stage]}', True, white)
    # 화면에 폰트가 표시되는 위치 설정
    screen.blit(text, (510, 5))
    # 화면 업데이트
    pygame.display.flip()

# 게임 종료
pygame.quit()

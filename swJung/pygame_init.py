import pygame
import time
from character import Character  # 캐릭터 모듈 import
from envrionment import Script
from sounds import Bgm
DEBUGGING = False  # 디버깅 모드 변수
# 게임초기화
pygame.init()

# 게임창 옵션 설정
background_size = (600, 900)  # 화면크기
screen = pygame.display.set_mode(background_size)  # 화면크기 세팅
title = 'My Game'
pygame.display.set_caption(title)  # 제목세팅

walk_sound = pygame.mixer.Sound(  # 소리세팅
    './sound/walksound.mp3')
door_sound = pygame.mixer.Sound(
    './sound/doorsound.mp3'
)
bgm = Bgm('./sound/background.mp3')

# 게임 내 필요한 설정
clock = pygame.time.Clock()  # 시간 변수 설정
black = (0, 0, 0)
white = (255, 255, 255)
color = black     # 색상설정 RGB
stage = 0

choices = [('Study', 'Art'),
           ('Major', 'Love'),
           ('Work', 'Family')]  # 선택지
select = []  # 선택지 저장
ch = Character(background_size, screen)  # 캐릭터 객체 설정
scripts = Script()  # 게임 환경 객체 설정


def door_dist(x, y):  # 문 을 여는 거리
    if 375 <= y <= 390 and 295 <= x <= 370:
        return 'Right'
    elif 375 <= y <= 390 and 100 <= x <= 175:
        return 'Left'


def door_open(key):
    global stage, Left
    bgm.pause_music()
    door_sound.play()
    walk_sound.stop()
    select.append(choices[stage][key])
    scripts.choice_script(choices[stage][key])
    scripts.enter_script(stage+1)
    ch.stage_chage()
    stage += 1
    bgm.unpause_music()
    Left = True


left_go = right_go = down_go = up_go = False  # 키 입력 변수

movement = 5  # 이동량
if not DEBUGGING:
    scripts.print_prologue()
scripts.enter_script(stage)
bgm.play_music()
# main event
Running = True  # 게임 진행 변수
Left = True
while Running:
    # FPS 설정
    clock.tick(60)  # while문 반복 1초에 60번 간격으로 설정
    try:
        background = pygame.image.load(f'./img/Room{stage+1}_final_cg.png')
    except FileNotFoundError:
        print("ERROR!!")
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
                if not Left:
                    ch.flip()
                    Left = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
                if Left:
                    ch.flip()
                    Left = False
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif door_dist(ch.x, ch.y) == 'Left' and pygame.K_SPACE:
                door_open(0)
            elif door_dist(ch.x, ch.y) == 'Right' and pygame.K_SPACE:
                door_open(1)
        elif event.type == pygame.KEYUP:  # key를 뗐을때
            walk_sound.fadeout(450)
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
        if ch.x <= 45:
            ch.x = 45
    elif right_go:
        ch.x += movement
        # if ch.x >= background_size[0]-ch.sx:
        if ch.x >= 435:
            ch.x = 435
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
    scripts.stage_status(stage)

# 게임 종료
pygame.quit()

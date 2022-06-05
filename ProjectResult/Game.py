import sys
import os
import pygame
from character import Character  # 캐릭터 모듈 import
from envrionment import Script  # 환경 모듈import
from sounds import Bgm  # 소리모듈 import

DEBUGGING = True  # 디버깅 모드 변수
Path = os.path.dirname(__file__)  # 파일 경로

# 색상설정 RGB
white = (255, 255, 255)
Black = (0, 0, 0)


# 게임초기화
pygame.init()

background_size = (600, 900)  # 화면크기
screen = pygame.display.set_mode(background_size)  # 화면크기 세팅

# 게임창 옵션 설정
title = 'Life(choice)'
pygame.display.set_caption(title)  # 제목세팅

walk_sound = pygame.mixer.Sound(  # 소리세팅
    os.path.join(Path, 'sound', 'walksound.mp3'))
walk_sound.set_volume(0.3)
door_sound = pygame.mixer.Sound(
    os.path.join(Path, 'sound', 'doorsound.mp3')
)
bgm = Bgm(os.path.join(Path, 'sound', 'background.mp3'))
ending_bgm = Bgm(os.path.join(Path, 'sound', 'endingbgm.mp3'))

# 게임 내 필요한 설정
scripts = Script(Path, screen)  # 스크립트 재생 객체 설정
ch = Character(background_size, screen, Path)  # 캐릭터 객체 설정

clock = pygame.time.Clock()  # 시간 변수 설정

stage = 1
choices = [('Study', 'Art'),
           ('Major', 'Love'),
           ('Work', 'Family')]  # 선택지
select = []  # 선택지 저장


# For Debug
# if DEBUGGING:
#     stage = 4
#     select = ['Study', 'Love', 'Work']
#     ch.age = 3


def door_dist(x, y):  # 문 을 여는 거리
    if 420 <= y <= 430 and 295 <= x <= 370:
        return 'Right'
        # 기존 375 <= y <= 390
    elif 420 <= y <= 430 and 100 <= x <= 175:
        return 'Left'


def door_open(key):
    global stage, Left_watching, left_go, right_go, down_go, up_go, playcount
    playcount = 0
    bgm.pause_music()
    door_sound.play()
    walk_sound.stop()
    scripts.choice_script(choices[stage-1][key])
    select.append(choices[stage-1][key])
    stage += 1
    scripts.enter_script(stage-1)
    ch.stage_chage()
    bgm.unpause_music()
    Left_watching = True
    left_go = right_go = down_go = up_go = False


left_go = right_go = down_go = up_go = False  # 키 입력 변수

movement = 5  # 이동량
walkcount = 0

if not DEBUGGING:
    scripts.print_prologue()
    scripts.enter_script(stage-1)
    bgm.play_music()

# main event
Running = True  # 게임 진행 변수q
Left_watching = True
stop_ck = True
walkcount_max = 20
playcount = 0
Ending = False
Starting = True

while Running:
    # FPS 설정
    clock.tick(60)  # while문 반복 1초에 60번 간격으로 설정
    if stage == 1 and Starting:
        scripts.show_tutorial('Title.png')
        scripts.print_prologue()
        scripts.show_tutorial('tutorial_manual.png')
        scripts.enter_script(stage-1)
        bgm.play_music()
        ch.init_position()
        Starting = False
    try:
        background = pygame.image.load(
            os.path.join(Path, 'img', f'Room{stage}_final_cg.png'))
    except FileNotFoundError:
        print("ERROR!!")
        break
    if stage == 4:  # 엔딩 임시구현 (자동걷기)
        bgm.stop_music()
        ending_bgm.play_music()
        Ending = True
        ch.set_position(45, 670)
        ch.flip()
        while Ending:
            ch.x += 5
            Left_watching = False
            stop_ck = False
            if ch.x >= 260:
                ch.x = 260
                ch.y -= 5
                if ch.y <= 585:
                    ch.y = 585
            screen.fill(Black)
            screen.blit(background, (0, 0))
            walkcount_max = 4
            walkcount = ch.walk(walkcount, Left_watching,
                                stop_ck, walkcount_max)
            ch.show(screen)  # 캐릭터를 스크린에 표시
            scripts.stage_status(stage-1)
            pygame.time.delay(250)
            if ch.y == 585:
                pygame.time.delay(3000)
                scripts.ending(select)
                Ending_roll = True
                while Ending_roll:
                    scripts.print_ending_script('다시 도전한다(r) / 게임을 끝낸다(q)')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                            elif event.key == pygame.K_r:
                                left_go = right_go = down_go = up_go = False
                                Ending = False
                                select = []
                                stage = 1
                                Starting = True
                                Left_watching = True
                                ending_bgm.stop_music()
                                ch.stage_chage()
                                Ending_roll = False
                                walkcount_max = 20
                                scripts.count = 0
                                playcount = 0
                                stop_ck = True  # 재시작시 움직이는 버그 수정
                                break
                            # 함수에select 리스트를 넘겨주면서 선택지에 따른
                            # 엔딩 출력 구현
                            # 입력감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit에 대한 명령일 경우 종료
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # key를 눌렀을때
            if event.key == pygame.K_LEFT:
                left_go = True
                if not Left_watching:
                    Left_watching = True
                stop_ck = False
                playcount += 1
            elif event.key == pygame.K_RIGHT:
                right_go = True
                if Left_watching:
                    Left_watching = False
                stop_ck = False
                playcount += 1
            elif event.key == pygame.K_UP:
                up_go = True
                stop_ck = False
                playcount += 1
            elif event.key == pygame.K_DOWN:
                down_go = True
                stop_ck = False
                playcount += 1
            elif door_dist(ch.x, ch.y) == 'Left' and event.key == pygame.K_SPACE:
                door_open(0)
            elif door_dist(ch.x, ch.y) == 'Right' and event.key == pygame.K_SPACE:
                door_open(1)
            if playcount == 1:
                walk_sound.play(-1)  # 걷는소리 재생
        elif event.type == pygame.KEYUP:  # key를 눌렀을때
            if event.key == pygame.K_LEFT:
                left_go = False
                playcount -= 1
            elif event.key == pygame.K_RIGHT:
                right_go = False
                playcount -= 1
            elif event.key == pygame.K_UP:
                up_go = False
                playcount -= 1
            elif event.key == pygame.K_DOWN:
                down_go = False
                playcount -= 1
            if playcount == 0:
                walk_sound.fadeout(700)

    # if not(right_go or left_go or up_go or down_go):
    #    stop_ck = True

    if left_go:
        ch.x -= movement
        if ch.x <= 40:
            ch.x = 40
    elif right_go:
        ch.x += movement
        # if ch.x >= background_size[0]-ch.sx:
        if ch.x >= 440:
            ch.x = 440
    elif up_go:
        ch.y -= movement
        if ch.y <= 430:
            ch.y = 430      # 기존 375
    elif down_go:
        ch.y += movement
        if ch.y >= background_size[1]-ch.sy-15:
            ch.y = background_size[1]-ch.sy-15
    else:
        stop_ck = True  # 모션버그, 키씹힘 수정

    if stage != 4:
        walkcount = ch.walk(walkcount, Left_watching, stop_ck, walkcount_max)

    if not DEBUGGING:  # 캐릭터 좌표 디버깅
        print(ch.x, ch.y)
        print(select)
        print(f'stage : {stage}')
    # 그리기
    screen.fill(Black)
    screen.blit(background, (0, 0))
    ch.show(screen)  # 캐릭터를 스크린에 표시
    scripts.stage_status(stage-1)


# 게임 종료
pygame.quit()

import pygame
import os

pygame.init()

background = pygame.display.set_mode((1000, 768))
pygame.display.set_caption("Life is Egg")

fps = pygame.time.Clock()


def game_text(word):
    font = pygame.font.SysFont('전주완판본각b', 40)

    text = font.render(word, True, (255, 255, 255))

    size_width_text = text.get_rect().size[0]
    size_height_text = text.get_rect().size[1]

    x_pos_text = background.get_size()[0]/2 - size_width_text/2
    y_pos_text = background.get_size()[1]/2 - size_height_text

    background.blit(text, (x_pos_text, y_pos_text))


start = True
prologue = ["어서오세요.", "게임에 참가하게 된 것을 환영합니다.", "방법은 지극히 간단합니다. 어렵지 않아요.", "앞으로 마주할 커다란 갈림길 앞에서…",
            "당신은 하나의 선택을 하게 될 것입니다.", "그리고 그 선택이 서로 다른 이야기를 만들고.", "서로 다른 결말을 낳겠죠.", "……우리 모두가 그렇듯이", "그럼, 출발합시다.", ]

h_img = os.path.join(os.getcwd(), 'img', f'1st_left_front_img.png')
image_human = pygame.image.load(h_img).convert_alpha()
image_human = pygame.transform.scale(image_human, (200, 200))
image_human_di = 0
human_walk_sound = pygame.mixer.Sound(
    os.path.join(os.getcwd(), 'sound', 'walksound.mp3'))

size_human_width = image_human.get_rect().size[0]
size_human_height = image_human.get_rect().size[1]

x_pos_human = background.get_size()[0]/2 - size_human_width/2
y_pos_human = background.get_size()[1] - size_human_height

door_sound = pygame.mixer.Sound(os.path.join(
    os.getcwd(), 'sound', 'doorsound.mp3'))

w_img = os.path.join(os.getcwd(), 'img', f'Room1_final.png')
image_wall = pygame.image.load(w_img).convert_alpha()
image_wall = pygame.transform.scale(image_wall, (1000, 768))

size_wall_width = image_wall.get_rect().size[0]
size_wall_height = image_wall.get_rect().size[1]

x_pos_wall = background.get_size()[0]/2 - size_wall_width/2
y_pos_wall = background.get_size()[1] - size_wall_height

background_sound = pygame.mixer.music.load(
    os.path.join(os.getcwd(), 'sound', 'background.mp3'))
pygame.mixer.music.set_volume(0.2)

to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(30)

    if start:
        start = False
        for i in prologue:
            background.fill((0, 0, 0))
            game_text(str(i))
            pygame.display.update()
            pygame.time.delay(1800)
        background.fill((0, 0, 0))
        game_text("<소년기>")
        pygame.mixer.music.play(-1)
        pygame.display.update()
        pygame.time.delay(1200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= 5
                pygame.mixer.Sound.play(human_walk_sound)
            elif event.key == pygame.K_DOWN:
                to_y += 5
                pygame.mixer.Sound.play(human_walk_sound)
            elif event.key == pygame.K_LEFT:
                to_x -= 5
                pygame.mixer.Sound.play(human_walk_sound)
                if image_human_di == 1:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
                    image_human_di = 0
            elif event.key == pygame.K_RIGHT:
                to_x += 5
                pygame.mixer.Sound.play(human_walk_sound)
                if image_human_di == 0:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
                    image_human_di = 1
            elif event.key == pygame.K_ESCAPE:
                play = False
            elif event.key == pygame.K_SPACE:
                if y_pos_human == 233 and x_pos_human >= 210 and x_pos_human <= 275:
                    pygame.mixer.Sound.stop(human_walk_sound)
                    pygame.mixer.Sound.play(door_sound)
                    background.fill((0, 0, 0))
                    game_text("무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.")
                    pygame.display.update()
                    pygame.time.delay(1800)
                    background.fill((0, 0, 0))
                    game_text("<청년기>")
                    pygame.display.update()
                    pygame.time.delay(1200)
                    h_img = os.path.join(
                        os.getcwd(), 'img', f'2nd_left_front_img.png')
                    image_human = pygame.image.load(h_img).convert_alpha()
                    image_human = pygame.transform.scale(
                        image_human, (200, 200))
                    image_human_di = 0
                    x_pos_human = background.get_size()[
                        0]/2 - size_human_width/2
                    y_pos_human = background.get_size()[1] - size_human_height

                    w_img = os.path.join(
                        os.getcwd(), 'img', f'Room2_final.png')
                    image_wall = pygame.image.load(w_img).convert_alpha()
                    image_wall = pygame.transform.scale(
                        image_wall, (1000, 768))

        if event.type == pygame.KEYUP:
            pygame.mixer.Sound.stop(human_walk_sound)
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0

    x_pos_human += to_x
    y_pos_human += to_y
    if y_pos_human <= 232:
        y_pos_human += 5
        pygame.mixer.Sound.stop(human_walk_sound)
    elif y_pos_human >= 577:
        y_pos_human -= 5
        pygame.mixer.Sound.stop(human_walk_sound)
    if x_pos_human <= 79:
        x_pos_human += 5
        pygame.mixer.Sound.stop(human_walk_sound)
    elif x_pos_human >= 718:
        x_pos_human -= 5
        pygame.mixer.Sound.stop(human_walk_sound)
    #print(x_pos_human, y_pos_human)

    background.fill((0, 0, 0))
    background.blit(image_wall, (x_pos_wall, y_pos_wall))
    background.blit(image_human, (x_pos_human, y_pos_human))
    pygame.display.update()

pygame.quit()

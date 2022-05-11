import pygame

pygame.init()

background = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Life is Egg")

fps = pygame.time.Clock()


def game_text(word):
    font = pygame.font.SysFont(None, 100)

    text = font.render(word, True, (0, 0, 0))

    size_width_text = text.get_rect().size[0]
    size_height_text = text.get_rect().size[1]

    x_pos_text = background.get_size()[0]/2 - size_width_text/2
    y_pos_text = background.get_size()[1]/2 - size_height_text/2

    background.blit(text, (x_pos_text, y_pos_text))


start = True
prologue = ["Welcome.", "게임에 참가하게 된 것을 환영합니다.",
            "방법은 지극히 간단합니다. 어렵지 않아요.", "앞으로 마주할 커다란 갈림길 앞에서…", "당신은 하나의 선택을 하게 될 것입니다.", "그리고 그 선택이 서로 다른 이야기를 만들고.", "서로 다른 결말을 낳겠죠.", "……우리 모두가 그렇듯이", "그럼, 출발합시다."]

image_human = pygame.image.load(
    "C:/Users/cksdn/project/cwLee/img/adolescence.png").convert_alpha()
image_human = pygame.transform.scale(image_human, (90, 90))
image_human_di = 0
human_walk_sound = pygame.mixer.music.load(
    "C:/Users/cksdn/project/cwLee/sound/walksound.mp3")
human_mask = pygame.mask.from_surface(image_human)

size_human_width = image_human.get_rect().size[0]
size_human_height = image_human.get_rect().size[1]

x_pos_human = background.get_size()[0]/2 - size_human_width/2
y_pos_human = background.get_size()[1] - size_human_height

image_wall = pygame.image.load(
    "C:/Users/cksdn/project/cwLee/img/wall.png").convert_alpha()
image_wall = pygame.transform.scale(image_wall, (500, 500))
wall_mask = pygame.mask.from_surface(image_wall)

size_wall_width = image_wall.get_rect().size[0]
size_wall_height = image_wall.get_rect().size[1]

x_pos_wall = background.get_size()[0]/2 - size_wall_width/2
y_pos_wall = background.get_size()[1] - size_wall_height

to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(60)

    if start:
        start = False
        for i in prologue:
            background.fill((255, 255, 255))
            game_text(str(i))
            pygame.display.update()
            pygame.time.delay(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.play(-1)
            if event.key == pygame.K_w:
                to_y -= 1.5
            elif event.key == pygame.K_s:
                to_y += 1.5
            elif event.key == pygame.K_a:
                to_x -= 1.5
                if image_human_di == 1:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
                    image_human_di = 0
            elif event.key == pygame.K_d:
                to_x += 1.5
                if image_human_di == 0:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
                    image_human_di = 1
            elif event.key == pygame.K_SPACE:
                image_human = pygame.image.load(
                    "C:/Users/cksdn/project/cwLee/img/adult.png")
                image_human = pygame.transform.scale(image_human, (90, 90))
                image_human_di = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                to_y = 0
            elif event.key == pygame.K_s:
                to_y = 0
            elif event.key == pygame.K_a:
                to_x = 0
            elif event.key == pygame.K_d:
                to_x = 0

    x_pos_human += to_x
    y_pos_human += to_y

    background.fill((0, 255, 0))
    background.blit(image_human, (x_pos_human, y_pos_human))
    background.blit(image_wall, (x_pos_wall, y_pos_wall))
    pygame.display.update()

pygame.quit()

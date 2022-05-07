import pygame

pygame.init()

background = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Life is Egg")

fps = pygame.time.Clock()

image_human = pygame.image.load(
    "C:/Users/cksdn/Desktop/cwLee/img/adolescence.png")
image_human = pygame.transform.scale(image_human, (90, 90))
image_human_di = 0
human_walk_sound = pygame.mixer.Sound(
    "C:/Users/cksdn/Desktop/cwLee/sound/walksound.mp3")
sound_play = 0

size_human_width = image_human.get_rect().size[0]
size_human_height = image_human.get_rect().size[1]

x_pos_human = background.get_size()[0]/2 - size_human_width/2
y_pos_human = background.get_size()[1] - size_human_height

to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if sound_play == 0:
                pygame.mixer.Sound.play(human_walk_sound)
                sound_play = 1
            if event.key == pygame.K_w:
                to_y -= 2
            elif event.key == pygame.K_s:
                to_y += 2
            elif event.key == pygame.K_a:
                to_x -= 2
                if image_human_di == 1:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
                    image_human_di = 0
            elif event.key == pygame.K_SPACE:
                image_human = pygame.image.load(
                    "C:/Users/cksdn/Desktop/cwLee/img/adult.png")
                image_human = pygame.transform.scale(image_human, (90, 90))
            elif event.key == pygame.K_d:
                to_x += 2
                if image_human_di == 0:
                    image_human = pygame.transform.flip(
                        image_human, True, False)
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
            pygame.mixer.Sound.stop(human_walk_sound)
            sound_play = 0

    x_pos_human += to_x
    y_pos_human += to_y

    background.fill((0, 255, 0))
    background.blit(image_human, (x_pos_human, y_pos_human))
    pygame.display.update()

pygame.quit()

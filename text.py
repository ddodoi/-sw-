import pygame

pygame.init()

background = pygame.display.set_mode((1000, 768))
pygame.display.set_caption("Text Test")

fps = pygame.time.Clock()

level = 0


def level_text(a, b):
    font = pygame.font.SysFont('전주완판본각b', 40)

    atext = font.render(a, True, (255, 255, 255))
    btext = font.render(b, True, (255, 255, 255))

    size_width_atext = atext.get_rect().size[0]
    size_height_atext = atext.get_rect().size[1]
    size_width_btext = btext.get_rect().size[0]
    size_height_btext = btext.get_rect().size[1]

    x_pos_atext = background.get_size()[0]/2 - size_width_atext/2
    y_pos_atext = background.get_size()[1]/4 - size_height_atext
    x_pos_btext = background.get_size()[0]/2 - size_width_btext/2
    y_pos_btext = background.get_size()[1]/2 + size_height_btext

    background.fill((0, 0, 0))
    background.blit(atext, (x_pos_atext, y_pos_atext))
    background.blit(btext, (x_pos_btext, y_pos_btext))
    pygame.display.update()
    pygame.time.delay(1800)

# prologue


selection_steps = [["<소년기>-공부", "무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.", "<소년기>-예체능", "당신의 끼를 발산하는 것을 좋아하는군요."],
                   ["<청년기>-전공", "당신은 꿈을 좇아 멈추지 않는군요.",
                    "<청년기>-연애", "청춘은 불같은 사랑 없이는 성립하지 않죠."],
                   ["<장년기>-일", "성공으로 보답하는 것만이 최고의 선택이죠.", "<장년기>-가족", "역시 곁에 있어 주는 가족이 최고죠."]]

# start_steps = [["<소년기>", "당신은 무럭무럭 자라 다른 아이들과 마찬가지로 학교에 다니게 되었습니다. 당신의 관심사는?"],
#["<청년기>", "스스로의 관심사에 맞추어 대학에 진학한 당신. 청춘의 한가운데 당신이 열중하는 것은?"],
# ["<장년기>", "인생의 반환점을 지나온 당신. 이제는 어디에 충실해야 할지 알 것 같은데?"]]

# ending

play = True
while play:
    deltaTime = fps.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False
            elif event.key == pygame.K_q:
                if level < 3:
                    level_text(selection_steps[level]
                               [0], selection_steps[level][1])
                    level += 1
            elif event.key == pygame.K_e:
                if level < 3:
                    level_text(selection_steps[level]
                               [2], selection_steps[level][3])
                    level += 1
        if level >= 3:
            pygame.time.delay(1200)
            level_text("<노년기>", "END")
            play = False

    background.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()

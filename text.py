import pygame

pygame.init()

background = pygame.display.set_mode((1000, 768))  # 배경화면 설정 가로: 1000 세로: 768
pygame.display.set_caption("Text Test")  # 제목

fps = pygame.time.Clock()  # 게임 속도

level = 0  # 단계 <소년기> = 0, <청년기> = 1, <장년기> = 2, <노년기> = 3


class text_print:
    def __init__(self):
        self.font = pygame.font.SysFont('전주완판본각b', 30)  # 폰트, 크기설정

    def twoline_text(self, a, b):  # 텍스트 2줄 출력함수
        atext = self.font.render(a, True, (255, 255, 255))  # 1번 문자열, 표면부드럽게, 색
        btext = self.font.render(b, True, (255, 255, 255))  # 2번 문자열, 표면부드럽게, 색

        size_width_atext = atext.get_rect().size[0]  # 1번 크기
        size_height_atext = atext.get_rect().size[1]  # 1번 높이
        size_width_btext = btext.get_rect().size[0]  # 2번 크기
        size_height_btext = btext.get_rect().size[1]  # 2번 높이

        x_pos_atext = background.get_size()[0]/2 - size_width_atext/2  # 1번 x좌표
        y_pos_atext = background.get_size()[1]/4 - size_height_atext  # 1번 y좌표
        x_pos_btext = background.get_size()[0]/2 - size_width_btext/2  # 2번 x좌표
        y_pos_btext = background.get_size()[1]/2 + size_height_btext  # 2번 y좌표

        background.fill((0, 0, 0))  # 배경화면 검은색
        background.blit(atext, (x_pos_atext, y_pos_atext))  # 1번 생성(x,y)
        background.blit(btext, (x_pos_btext, y_pos_btext))  # 2번 생성(x,y)
        pygame.display.update()  # 변경사항 화면반영

# prologue =


# 단계시작 출력 문자열
start_steps = [["<소년기>", "당신은 무럭무럭 자라 다른 아이들과 마찬가지로 학교에 다니게 되었습니다.", "당신의 관심사는?"],
               ["<청년기>", "스스로의 관심사에 맞추어 대학에 진학한 당신.", "청춘의 한가운데 당신이 열중하는 것은?"],
               ["<장년기>", "인생의 반환점을 지나온 당신.", "이제는 어디에 충실해야 할지 알 것 같은데?"]]


# 선택한 분기의 문자열
selection_steps = [["<소년기>-공부", "무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.", "<소년기>-예체능", "당신의 끼를 발산하는 것을 좋아하는군요."],
                   ["<청년기>-전공", "당신은 꿈을 좇아 멈추지 않는군요.",
                    "<청년기>-연애", "청춘은 불같은 사랑 없이는 성립하지 않죠."],
                   ["<장년기>-일", "성공으로 보답하는 것만이 최고의 선택이죠.", "<장년기>-가족", "역시 곁에 있어 주는 가족이 최고죠."]]

# epilogue

# ending

background.fill((0, 0, 0))
pygame.display.update()

play = True
while play:  # play가 True일동안 출력
    deltaTime = fps.tick(30)  # 게임속도 30프레임
    for event in pygame.event.get():  # 파이게임 이벤트
        if event.type == pygame.QUIT:  # 파이게임을 끄면 종료
            play = False
        if event.type == pygame.KEYDOWN:  # 키보드를 누름
            if event.key == pygame.K_ESCAPE:  # esc누르면 종료
                play = False
            elif event.key == pygame.K_q:  # q를 누르면 왼쪽 분기 선택, 문자열 출력, 단계 상승
                if level < 3:
                    twoline_text(selection_steps[level]
                                 [0], selection_steps[level][1])
                    level += 1
                    pygame.time.delay(1800)  # 1.8초 대기 (1/1000초)
            elif event.key == pygame.K_e:  # e를 누르면 왼쪽 분기 선택, 문자열 출력, 단계 상승
                if level < 3:
                    twoline_text(selection_steps[level]
                                 [2], selection_steps[level][3])
                    level += 1
                    pygame.time.delay(1800)  # 1.8초 대기 (1/1000초)
        if level >= 3:  # 노년기가 되면 게임 종료
            pygame.time.delay(1200)
            twoline_text("<노년기>", "END")
            play = False

    twoline_text(start_steps[level][0], start_steps[level][1])
    pygame.time.delay(1000)

pygame.quit()  # 파이게임 종료

import pygame

pygame.init()

background = pygame.display.set_mode((1000, 768))  # 배경화면 설정 가로: 1000 세로: 768
pygame.display.set_caption("Prototype")  # 제목

fps = pygame.time.Clock()  # 게임 속도


class text_print:
    def __init__(self):
        self.font = pygame.font.SysFont('전주완판본각b', 30)  # 폰트, 크기설정

    def oneline_text(self, a):  # 텍스트 2줄 출력함수
        atext = self.font.render(a, True, (255, 255, 255))  # 1번 문자열, 표면부드럽게, 색

        size_width_atext = atext.get_rect().size[0]  # 1번 크기
        size_height_atext = atext.get_rect().size[1]  # 1번 높이

        x_pos_atext = background.get_size()[0]/2 - size_width_atext/2  # 1번 x좌표
        y_pos_atext = background.get_size()[1]/2 - size_height_atext  # 1번 y좌표

        background.fill((0, 0, 0))  # 배경화면 검은색
        background.blit(atext, (x_pos_atext, y_pos_atext))  # 1번 생성(x,y)
        pygame.display.update()  # 변경사항 화면반영

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

    def ep_text(self, a):
        b = "이미지"
        atext = self.font.render(a, True, (255, 255, 255))  # 1번 문자열, 표면부드럽게, 색
        btext = self.font.render(b, True, (255, 255, 255))  # 2번 문자열, 표면부드럽게, 색

        size_width_atext = atext.get_rect().size[0]  # 1번 크기
        size_height_atext = atext.get_rect().size[1]  # 1번 높이
        size_width_btext = btext.get_rect().size[0]  # 2번 크기
        size_height_btext = btext.get_rect().size[1]  # 2번 높이

        x_pos_atext = background.get_size()[0]/2 - size_width_atext/2  # 1번 x좌표
        y_pos_atext = background.get_size()[1] - size_height_atext*2  # 1번 y좌표
        x_pos_btext = background.get_size()[0]/2 - size_width_btext/2  # 2번 x좌표
        y_pos_btext = background.get_size()[1]/4 + size_height_btext  # 2번 y좌표

        background.fill((0, 0, 0))  # 배경화면 검은색
        background.blit(atext, (x_pos_atext, y_pos_atext))  # 1번 생성(x,y)
        background.blit(btext, (x_pos_btext, y_pos_btext))  # 2번 생성(x,y)
        pygame.display.update()  # 변경사항 화면반영
    '''
    def ed_text(self, a, b, c, d, e, f):
        atext = self.font.render(a, True, (255, 255, 255))  # 1번 문자열, 표면부드럽게, 색
        btext = self.font.render(b, True, (255, 255, 255))  # 2번 문자열, 표면부드럽게, 색
        ctext = self.font.render(c, True, (255, 255, 255))  # 3번 문자열, 표면부드럽게, 색
        dtext = self.font.render(d, True, (255, 255, 255))  # 4번 문자열, 표면부드럽게, 색
        etext = self.font.render(e, True, (255, 255, 255))  # 5번 문자열, 표면부드럽게, 색
        ftext = self.font.render(f, True, (255, 255, 255))  # 6번 문자열, 표면부드럽게, 색

        size_width_atext = atext.get_rect().size[0]  # 1번 크기
        size_height_atext = atext.get_rect().size[1]  # 1번 높이
        for i in range(11):
            x_pos_atext = background.get_size(
            )[0]/2 - size_width_atext  # 1번 x좌표
            y_pos_atext = background.get_size(
            )[1]/4 - size_height_atext  # 1번 y좌표
            x_pos_btext = x_pos_ctext = x_pos_ctext = x_pos_dtext = x_pos_etext = x_pos_ftext = x_pos_atext
            y_pos_btext = y_pos_atext - (size_width_atext * 2)
            y_pos_ctext = y_pos_btext - (size_width_atext * 2)
            y_pos_dtext = y_pos_ctext - (size_width_atext * 2)
            y_pos_etext = y_pos_dtext - (size_width_atext * 2)
            y_pos_ftext = y_pos_etext - (size_width_atext * 2)

            background.fill((0, 0, 0))  # 배경화면 검은색
            background.blit(atext, (x_pos_atext, y_pos_atext))  # 1번 생성(x,y)
            background.blit(btext, (x_pos_btext, y_pos_btext))  # 2번 생성(x,y)
            background.blit(ctext, (x_pos_ctext, y_pos_ctext))
            background.blit(dtext, (x_pos_dtext, y_pos_dtext))
            background.blit(etext, (x_pos_etext, y_pos_etext))
            background.blit(ftext, (x_pos_ftext, y_pos_ftext))
            pygame.display.update()  # 변경사항 화면반영
            y_pos_atext += 0.1
            pygame.time.delay(1000)
    '''


# 프롤로그 출력 문자열
prologue = ["어서오세요.", "게임에 참가하게 된 것을 환영합니다.",
            "방법은 지극히 간단합니다. 어렵지 않아요.",
            "앞으로 마주할 커다란 갈림길 앞에서…",
            "당신은 하나의 선택을 하게 될 것입니다.",
            "그리고 그 선택이 서로 다른 이야기를 만들고.",
            "서로 다른 결말을 낳겠죠.",
            "……우리 모두가 그렇듯이",
            "그럼, 출발합시다.", ]


# 단계시작 출력 문자열
start_steps = [["<소년기>", "당신은 무럭무럭 자라 다른 아이들과 마찬가지로 학교에 다니게 되었습니다.", "당신의 관심사는?", "←공부(q)   (e)예체능→"],
               ["<청년기>", "스스로의 관심사에 맞추어 대학에 진학한 당신.",
                   "청춘의 한가운데 당신이 열중하는 것은?", "←전공(q)   (e)연애→"],
               ["<장년기>", "인생의 반환점을 지나온 당신.", "이제는 어디에 충실해야 할지 알 것 같은데?", "←일(q)   (e)가정→"]]


# 선택한 분기의 문자열
selection_steps = [["<소년기>-공부", "무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.",
                    "<소년기>-예체능", "당신의 끼를 발산하는 것을 좋아하는군요."],
                   ["<청년기>-전공", "당신은 꿈을 좇아 멈추지 않는군요.",
                    "<청년기>-연애", "청춘은 불같은 사랑 없이는 성립하지 않죠."],
                   ["<장년기>-일", "성공으로 보답하는 것만이 최고의 선택이죠.",
                    "<장년기>-가족", "역시 곁에 있어 주는 가족이 최고죠."]]

# 주마등 문자열
epilogue = [["<소년기>-공부", "<청년기>-전공", "<장년기>-일"],
            ["<소년기>-공부", "<청년기>-전공", "<장년기>-가족"],
            ["<소년기>-공부", "<청년기>-연애", "<장년기>-일"],
            ["<소년기>-공부", "<청년기>-연애", "<장년기>-가족"],
            ["<소년기>-예체능", "<청년기>-전공", "<장년기>-일"],
            ["<소년기>-예체능", "<청년기>-전공", "<장년기>-가족"],
            ["<소년기>-예체능", "<청년기>-연애", "<장년기>-일"],
            ["<소년기>-예체능", "<청년기>-연애", "<장년기>-가족"]]

ending = [["(공부+전공+일 선택)", "어릴 때부터 확고한 관심사를 가졌던 당신은", "자연스레 목표를 이루기 위해 최선을 다했어요.", "그 결과 최고의 자리까지 올라갔지만……", "조금은 쓸쓸한 인생이었을지도 모르겠네요.", "수고했어요."],
          ["(공부+전공+가정 선택)", "어릴 때부터 확고한 관심사를 가졌던 당신은", "청춘을 불사르며 열심히 노력했어요.",
           "하지만 가족의 소중함 역시 깨달은 것 같네요.", "나쁘지 않아요.", "수고했어요."],
          ["(공부+사랑+일 선택)", "학구열이 강한 당신은", "열심히 공부하여 대학에 진학했고,", "그곳에서 진정한 사랑을 만나 뜨거운 청춘을 보냈군요.",
           "나이가 들어선 다시 일에 열중했지만,", "그래도 당신은 젊은 날을 추억하며 미소짓고 있네요."],
          ["(공부+사랑+가정 선택)", "학구열이 강한 당신은", "열심히 공부하여 대학에 진학했지만,", "진정한 사랑을 만나 뜨거운 청춘을 보냈군요.",
           "나이가 들어서도 가정에 충실하며 좋은 부모이자 배우자였네요.", "당신의 삶은 분명 꽤 따뜻했겠네요.", ],
          ["(예체능+전공+일 선택)", "통통 튀는 재능이 있는 당신은", "청춘을 모두 바쳐 세계적으로 유명한 인재가 되었군요.",
           "지금은 당신의 삶을 모두가 우러러보고 있어요.", "훌륭해요.", " "],
          ["(예체능+전공+가정 선택)", "통통 튀는 재능이 있는 당신은", "청춘을 바쳐 그 재능에 충실했지만,",
           "나이가 들어선 그 이상으로 가치있는 것을 찾아냈군요.", "가족의 품 만한 게 또 없죠."],
          ["(예체능+사랑+일 선택)", "주체할 수 없는 끼를 가진 당신은", "그 열정을 연인에게 쏟기로 결심했어요.",
           "나이가 들어선 다시 일에 충실했지만,", "그 청춘의 한 페이지가 어디 가는 것은 아니죠.", " "],
          ["(예체능+사랑+가정 선택)", "주체할 수 없는 끼를 가진 당신은", "그 열정을 연인에게 쏟기로 결심했고,", "나이가 들어서도 사랑하는 사람에겐", " 늘 최선을 다했군요.", "당신의 선택을 존중하고 축복해요."]]


curtaincall = ["이상입니다.",
               "즐거운 삶이었나요?",
               "부디 그러셨길 바랄게요.",
               "인생에 정답은 없으니까요.",
               "그래도 다시 한번 돌아간다면……",
               ">다시 도전한다/게임을 끝낸다"]

level = 0  # 단계 <소년기> = 0, <청년기> = 1, <장년기> = 2, <노년기> = 3

choice = [[0, 4],  # 공부 = 0, 예체능 = 4
          [-6, -4],  # 전공 = -6, 연애 = -4
          [6, 7]]  # 일 = 6, 가족 = 7

test = text_print()
ep = 0
start = True
key = True
play = True

background.fill((0, 0, 0))
pygame.display.update()

while play:  # play가 True일동안 출력
    deltaTime = fps.tick(30)  # 게임속도 30프레임
    if start:
        start = False
        for i in prologue:
            test.oneline_text(i)
            pygame.time.delay(1000)
        background.fill((0, 0, 0))
    for event in pygame.event.get():  # 파이게임 이벤트
        if event.type == pygame.QUIT:  # 파이게임을 끄면 종료
            play = False
        if event.type == pygame.KEYDOWN:  # 키보드를 누름
            if event.key == pygame.K_ESCAPE:  # esc누르면 종료
                play = False
            elif event.key == pygame.K_q:  # q를 누르면 왼쪽 분기 선택, 문자열 출력, 단계 상승
                if level < 3:
                    test.twoline_text(selection_steps[level]
                                      [0], selection_steps[level][1])
                    ep += choice[level][0]
                    level += 1
                    key = True
                    pygame.time.delay(1000)  # 1초 대기 (1/1000초)
            elif event.key == pygame.K_e:  # e를 누르면 왼쪽 분기 선택, 문자열 출력, 단계 상승
                if level < 3:
                    test.twoline_text(selection_steps[level]
                                      [2], selection_steps[level][3])
                    ep += choice[level][1]
                    level += 1
                    pygame.time.delay(1000)  # 1초 대기 (1/1000초)
        if level == 3:  # 노년기가 되면 게임 종료
            test.twoline_text("<노년기>", "END")
            pygame.time.delay(1000)
            for i in range(3):
                test.ep_text(epilogue[ep][i])
                pygame.time.delay(1000)
            '''test.ed_text(ending[ep][0], ending[ep][1],
                         ending[ep][2], ending[ep][3], ending[ep][4], ending[ep][5])'''
            for i in curtaincall:
                test.oneline_text(i)
                pygame.time.delay(1000)
            play = False
            level += 1
        elif level < 3 and key:
            test.twoline_text(start_steps[level][0], start_steps[level][1])
            pygame.time.delay(1000)
            test.twoline_text(start_steps[level][2], start_steps[level][3])
            pygame.time.delay(1000)
            key = False

pygame.quit()  # 파이게임 종료

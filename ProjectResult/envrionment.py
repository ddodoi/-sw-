import pygame
import os
import sys
# pygame.init()

# background_size = (600, 900)  # 화면크기
# screen = pygame.display.set_mode(background_size)  # 화면크기 세팅
# title = 'Life(choice)'
# pygame.display.set_caption(title)  # 제목세팅

Black = (0, 0, 0)
white = (255, 255, 255)


class Script:
    def __init__(self, Path, screen):
        self.Path = Path
        self.address = os.path.join(
            self.Path, 'font', 'DungGeunMo.ttf')
        self.stage_name = ['<소년기>', '<청년기>',
                           '<장년기>', '<노년기>']
        self.count = 0
        self.screen = screen

    def pass_over(self):
        loop = True
        self.count += 1
        color = Black
        while loop:
            if self.count != 11:
                if color == white:
                    color = Black
                else:
                    color = white
                pygame.draw.polygon(self.screen, color, [
                                    [300, 500], [308, 488], [292, 488]])
                pygame.display.update()
                pygame.time.delay(400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    loop = False
                    if self.count != 11:
                        pygame.draw.polygon(self.screen, Black, [
                                            [300, 500], [308, 488], [292, 488]])
                        pygame.display.update()
                pygame.time.delay(100)

    def print_prologue(self):
        prologue = ["어서오세요.",
                    "게임에 참가하게 된 것을 환영합니다.",
                    "방법은 지극히 간단합니다. 어렵지 않아요.",
                    "앞으로 마주할 커다란 갈림길 앞에서…",
                    "당신은 하나의 선택을 하게 될 것입니다.",
                    "그리고 그 선택이 서로 다른 이야기를 만들고.",
                    "서로 다른 결말을 낳겠죠.",
                    "……우리 모두가 그렇듯이",
                    "그럼, 출발합시다."]
        font = pygame.font.Font(self.address, 17)
        for line in prologue:
            self.screen.fill(Black)
            text = font.render(line, True, white)
            size_width_text = text.get_rect().size[0]
            size_height_text = text.get_rect().size[1]
            x_pos_text = round(self.screen.get_size()[0]/2 - size_width_text/2)
            y_pos_text = self.screen.get_size()[1]/2 - size_height_text
            self.screen.blit(text, (x_pos_text, y_pos_text))
            pygame.display.flip()
            self.pass_over()

    def enter_script(self, stage):
        script_lst = ['', '<소년기>',
                      '당신은 무럭무럭 자라 다른 아이들과 마찬가지로 학교에 다니게 되었습니다.',
                      '당신의 관심사는?',
                      '<청년기>', '스스로의 관심사에 맞추어 대학에 진학한 당신.',
                      '청춘의 한가운데 당신이 열중하는 것은?',
                      '<장년기>', '인생의 반환점을 지나온 당신.',
                      '이제는 어디에 충실해야 할지 알 것 같은데?',
                      '수고하셨습니다.',
                      '……슬슬 엔딩이 다가오고 있어요.',
                      '당신은…….',
                      '']
        try:
            font = pygame.font.Font(self.address, 16)
            for i in range(1, 4):
                self.screen.fill(Black)
                text = font.render(script_lst[3*stage+i], True, white)
                size_width_text = text.get_rect().size[0]
                size_height_text = text.get_rect().size[1]
                x_pos_text = round(self.screen.get_size()[
                                   0]/2 - size_width_text/2)
                y_pos_text = self.screen.get_size()[1]/2 - size_height_text
                self.screen.blit(text, (x_pos_text, y_pos_text))
                pygame.display.flip()
                self.pass_over()
        except IndexError:
            print('Error!!')

    def choice_script(self, key):
        script_dct = {'Study': '무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.',
                      'Art': '당신의 끼를 발산하는 것을 좋아하는군요.',
                      'Major': '당신은 꿈을 좇아 멈추지 않는군요.',
                      'Love': '청춘은 불같은 사랑 없이는 성립하지 않죠.',
                      'Work': '성공으로 보답하는 것만이 최고의 선택이죠.',
                      'Family': '역시 곁에 있어 주는 가족이 최고죠.'
                      }
        self.screen.fill(Black)
        font = pygame.font.Font(self.address, 17)
        text = font.render(script_dct[key], True, white)
        size_width_text = text.get_rect().size[0]
        size_height_text = text.get_rect().size[1]
        x_pos_text = round(self.screen.get_size()[0]/2 - size_width_text/2)
        y_pos_text = self.screen.get_size()[1]/2 - size_height_text
        self.screen.blit(text, (x_pos_text, y_pos_text))
        pygame.display.flip()
        self.pass_over()

    def stage_status(self, stage):
        # 폰트설정
        font = pygame.font.Font(self.address, 20)
        # 폰트를 이미지로 변경
        text = font.render(f'{self.stage_name[stage]}', True, white)
        # 화면에 폰트가 표시되는 위치 설정
        self.screen.blit(text, (510, 10))  # 기존 (510,5)
        # 화면 업데이트
        pygame.display.update()

    def ending(self, select):
        sc_list_1 = ['학구열이 강한 당신은 열심히 공부하여 대학에 진학했고',
                     '그곳에서 진정한 사랑을 만나 뜨거운 청춘을 보냈군요',
                     ' 나이가 들어선 다시 일에 열중했지만,',
                     '그래도 당신은 젊은 날을 추억하며 미소짓고 있네요',
                     '나이가 들어서도 가정에 충실하며', '좋은부모이자 배우자 였네요.',
                     '당신의 삶은 분명 꽤 따뜻했겠네요.']
        sc_list_2 = ['통통 튀는 재능이 있는 당신은',
                     '청춘을 모두 바쳐 세계적으로 유명한 인재가 되었군요.',
                     '지금은 당신의 삶을 모두가 우러러보고 있어요.',
                     '훌륭해요.',
                     '청춘을 바쳐 그 재능에 충실했지만,',
                     '나이가 들어선 그 이상으로 가치있는 것을 찾아냈군요.',
                     '가족의 품 만한 게 또 없죠.'
                     ]
        sc_list_3 = ['통통 튀는 재능이 있는 당신은',
                     '그 열정을 연인에게 쏟기로 결심했어요.',
                     '나이가 들어선 다시 일에 충실했지만,',
                     '그 청춘의 한 페이지가 어디 가는 것은 아니죠.',
                     '나이가 들어서도 사랑하는 사람에겐 늘 최선을 다했군요.',
                     '당신의 선택을 존중하고 축복해요.'
                     ]
        sc_list_4 = ['어릴 때부터 확고한 관심사를 가졌던 당신은',
                     '청춘을 불사르며 열심히 노력했어요.',
                     '그 결과 최고의 자리까지 올라갔지만……',
                     '조금은 쓸쓸한 인생이었을지도 모르겠네요.',
                     '수고했어요.',
                     '하지만 가족의 소중함 역시 깨달은 것 같네요.',
                     '나쁘지 않아요.',
                     '수고했어요.'
                     ]
        sc_list_5 = ['이상입니다.',
                     '즐거운 삶이었나요?',
                     '부디 그러셨길 바랄게요.',
                     '정답은 없으니까요.',
                     '그래도 다시 한번 돌아간다면…….']
        if select[0] == 'Study' and select[1] == 'Love':
            self.show_ending_scene('Study')
            self.print_ending_script(sc_list_1[0])
            self.pass_over()
            self.show_ending_scene('Love')
            self.print_ending_script(sc_list_1[1])
            self.pass_over()
            if select[2] == 'Work':
                self.show_ending_scene('Work')
                self.print_ending_script(sc_list_1[2])
                self.pass_over()
                self.print_ending_script(sc_list_1[3])
                self.pass_over()
            elif select[2] == 'Family':
                self.show_ending_scene('Family')
                self.print_ending_script(sc_list_1[4])
                self.pass_over()
                self.print_ending_script(sc_list_1[5])
                self.pass_over()
        elif select[0] == 'Art' and select[1] == 'Major':
            self.show_ending_scene('Art')
            self.print_ending_script(sc_list_2[0])
            self.pass_over()
            self.show_ending_scene('Major')
            if select[2] == 'Work':
                self.show_ending_scene('Work')
                for i in range(1, 4):
                    self.print_ending_script(sc_list_2[i])
                    self.pass_over()
            elif select[2] == 'Family':
                self.show_ending_scene('Family')
                for i in range(4, 7):
                    self.print_ending_script(sc_list_2[i])
                    self.pass_over()
        elif select[0] == 'Art' and select[1] == 'Love':
            self.show_ending_scene('Art')
            self.print_ending_script(sc_list_3[0])
            self.pass_over()
            self.show_ending_scene('Love')
            self.print_ending_script(sc_list_3[1])
            self.pass_over()
            if select[2] == 'Work':
                self.show_ending_scene('Work')
                self.print_ending_script(sc_list_3[2])
                self.pass_over()
                self.print_ending_script(sc_list_3[3])
                self.pass_over()
            elif select[2] == 'Family':
                self.show_ending_scene('Family')
                self.print_ending_script(sc_list_3[4])
                self.pass_over()
                self.print_ending_script(sc_list_3[5])
                self.pass_over()
        else:
            self.show_ending_scene('Study')
            self.print_ending_script(sc_list_4[0])
            self.pass_over()
            self.show_ending_scene('Major')
            self.print_ending_script(sc_list_4[1])
            self.pass_over()
            if select[2] == 'Work':
                self.show_ending_scene('Work')
                for i in range(2, 5):
                    self.print_ending_script(sc_list_4[i])
                    self.pass_over()
            elif select[2] == 'Family':
                self.show_ending_scene('Family')
                for i in range(5, 8):
                    self.print_ending_script(sc_list_4[i])
                    self.pass_over()
        for endscript in sc_list_5:
            self.print_ending_script(endscript)
            self.pass_over()

    def print_ending_script(self, stages):
        font = pygame.font.Font(self.address, 17)
        text = font.render(stages, True, white)
        self.screen.fill(Black)
        size_width_text = text.get_rect().size[0]
        size_height_text = text.get_rect().size[1]
        x_pos_text = round(self.screen.get_size()[0]/2 - size_width_text/2)
        y_pos_text = self.screen.get_size()[1]/2 - size_height_text
        self.screen.blit(text, (x_pos_text, y_pos_text))
        pygame.display.flip()

    def show_tutorial(self, image):
        self.screen.fill(Black)
        title = pygame.image.load(
            os.path.join(self.Path, 'img', image))
        self.screen.blit(title, (0, 0))
        pygame.display.flip()
        self.pass_over()

    def show_ending_scene(self, scene):
        scene_path = os.path.join(
            self.Path, 'img', 'ending_scene', f'{scene}.png')
        scene_img = pygame.image.load(scene_path)
        scene_img = pygame.transform.scale(scene_img, (400, 400))
        size_width_img = scene_img.get_rect().size[0]
        size_height_img = scene_img.get_rect().size[1]
        x_pos_img = round(self.screen.get_size()[0]/2 - size_width_img/2)
        y_pos_img = self.screen.get_size()[1]/2 - size_height_img+150
        for opacity in range(255, -1, -1):
            self.screen.fill(Black)
            scene_img.set_alpha(opacity)
            self.screen.blit(scene_img, (x_pos_img, y_pos_img))
            pygame.display.flip()
            pygame.time.delay(20)
        pygame.time.delay(1000)


if __name__ == '__main__':
    print('This is environment module')

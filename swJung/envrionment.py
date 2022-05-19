import pygame
import os
pygame.init()

background_size = (600, 900)  # 화면크기
screen = pygame.display.set_mode(background_size)  # 화면크기 세팅
title = 'My Game'
pygame.display.set_caption(title)  # 제목세팅

Black = (0, 0, 0)
white = (255, 255, 255)


class Script:
    def __init__(self):
        self.Path = os.getcwd()
        self.address = os.path.join(
            self.Path, 'font', 'DungGeunMo.ttf')

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
            screen.fill(Black)
            text = font.render(line, True, white)
            size_width_text = text.get_rect().size[0]
            size_height_text = text.get_rect().size[1]
            x_pos_text = round(screen.get_size()[0]/2 - size_width_text/2)
            y_pos_text = screen.get_size()[1]/2 - size_height_text
            screen.blit(text, (x_pos_text, y_pos_text))
            pygame.display.flip()
            pygame.time.delay(3000)

    def enter_script(self, stage):
        script_lst = ['', '<소년기>',
                      '당신은 무럭무럭 자라 다른 아이들과 마찬가지로 학교에 다니게 되었습니다.',
                      '당신의 관심사는?',
                      '<청년기>', '스스로의 관심사에 맞추어 대학에 진학한 당신.',
                      '청춘의 한가운데 당신이 열중하는 것은?',
                      '<장년기>', '인생의 반환점을 지나온 당신.',
                      '이제는 어디에 충실해야 할지 알 것 같은데?', '']
        try:
            font = pygame.font.Font(self.address, 16)
            for i in range(1, 4):
                screen.fill(Black)
                text = font.render(script_lst[3*stage+i], True, white)
                size_width_text = text.get_rect().size[0]
                size_height_text = text.get_rect().size[1]
                x_pos_text = round(screen.get_size()[0]/2 - size_width_text/2)
                y_pos_text = screen.get_size()[1]/2 - size_height_text
                screen.blit(text, (x_pos_text, y_pos_text))
                pygame.display.flip()
                pygame.time.delay(3000)
        except IndexError:
            return None

    def choice_script(self, key):
        script_dct = {'Study': '무언가를 배우고 좋은 성적을 받는 것을 좋아하는군요.',
                      'Art': '당신의 끼를 발산하는 것을 좋아하는군요.',
                      'Major': '당신은 꿈을 좇아 멈추지 않는군요.',
                      'Love': '청춘은 불같은 사랑 없이는 성립하지 않죠.',
                      'Work': '성공으로 보답하는 것만이 최고의 선택이죠.',
                      'Family': '역시 곁에 있어 주는 가족이 최고죠.'
                      }
        screen.fill(Black)
        font = pygame.font.Font(self.address, 17)
        text = font.render(script_dct[key], True, white)
        size_width_text = text.get_rect().size[0]
        size_height_text = text.get_rect().size[1]
        x_pos_text = round(screen.get_size()[0]/2 - size_width_text/2)
        y_pos_text = screen.get_size()[1]/2 - size_height_text
        screen.blit(text, (x_pos_text, y_pos_text))
        pygame.display.flip()
        pygame.time.delay(3000)

    def stage_status(self, stage):
        stage_name = ['<소년기>', '<청년기>',
                      '<장년기>', '<노년기>']
        # 폰트설정
        font = pygame.font.Font(self.address, 20)
        # 폰트를 이미지로 변경
        text = font.render(f'{stage_name[stage]}', True, white)
        # 화면에 폰트가 표시되는 위치 설정
        screen.blit(text, (510, 10))  # 기존 (510,5)
        # 화면 업데이트
        pygame.display.flip()

    def print_ending(self, select):
        pass


if __name__ == '__main__':
    print('This is environment module')

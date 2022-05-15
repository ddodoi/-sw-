import pygame
import time


class Env:
    def __init__(self):
        self.round = 1

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
        for pro in prologue:

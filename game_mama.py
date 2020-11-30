import random
import sys

import pygame
from PyQt5.QtWidgets import *

class Game_mama(QWidget):
    def __init__(self):
        super().__init__()
        pygame.init() #초기화 반드시 필요함
        self.initUI()

    def initUI(self):

        screen_width = 480
        SCREEN_HEIGHT = 640
        screen = pygame.display.set_mode((screen_width, SCREEN_HEIGHT))  # 화면 크기 설정
        clock = pygame.time.Clock()

        # 변수
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        small_font = pygame.font.SysFont('malgungothic', 35)
        score = 0
        shooted = 0
        game_over = False

        background_image = pygame.image.load("image/game_back.jpg")

        bad_image = pygame.image.load("image/sandwich.png")
        bads = []

        for i in range(4):
            bad = bad_image.get_rect(left=random.randint(0, screen_width - bad_image.get_width()), top=-100)
            dy = random.randint(3, 9)
            bads.append((bad, dy))

        fighter_image = pygame.image.load("image/game_baby.png") #도망 다니는 아이
        fighter = fighter_image.get_rect(centerx=screen_width // 2, bottom=SCREEN_HEIGHT)

        # pygame.mixer.init()
        # pygame.mixer.music.load('music.mid') #배경 음악
        # pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
        # missile_sound = pygame.mixer.Sound('missile.wav') #사운드
        # explosion_sound = pygame.mixer.Sound('explosion.wav')
        # game_over_sound = pygame.mixer.Sound('game_over.wav')

        running = True

        while running:  # 게임 루프
            screen.blit(background_image, (0, 0))

            # 변수 업데이트

            event = pygame.event.poll()  # 이벤트 처리
            if event.type == pygame.QUIT:
                break

            pressed = pygame.key.get_pressed() # 화살표가 눌렸을 때 변수

            if pressed[pygame.K_LEFT]: #왼쪽 키가 눌리고 게임이 끝나지 않
                fighter.left -= 5
            elif pressed[pygame.K_RIGHT]:
                fighter.left += 5

            if not game_over:
                for bad, dy in bads:
                    bad.top += dy
                    if bad.top > SCREEN_HEIGHT:
                        bads.remove((bad, dy))
                        bad = bad_image.get_rect(left=random.randint(0, screen_width - bad_image.get_width()),
                                                   top=-100)
                        dy = random.randint(3, 9)
                        bads.append((bad, dy))
                        shooted += 1

                if fighter.left < 0:
                    fighter.left = 0

                elif fighter.right > screen_width:
                    fighter.right = screen_width

                for bad, dy in bads:
                    if bad.colliderect(fighter):
                        # print('충돌')
                        # print(bad)
                        # print(fighter)
                        running = False
                        pygame.mixer.music.stop()

            # 화면 그리기

            for bad, dy in bads:
                screen.blit(bad_image, bad)

            screen.blit(fighter_image, fighter)

            score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
            screen.blit(score_image, (10, 10))

            if running==False:
                game_over_image = small_font.render('게임 종료', True, RED)
                game_over_image1 = small_font.render(' score : {}'.format(score), True, RED)
                screen.blit(game_over_image, game_over_image.get_rect(centerx=screen_width // 2 , centery=SCREEN_HEIGHT // 2 - 50))
                screen.blit(game_over_image1, game_over_image1.get_rect(centerx=screen_width // 2, centery=SCREEN_HEIGHT // 2))

            pygame.display.update()  # 모든 화면 수시로 업데이트
            clock.tick(60)  # 초당 프레임
        pygame.time.delay(2000) #2초의 약간 딜레이

        pygame.quit()

    def closeEvent(self, event): #종료 이벤트
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__=="__main__":
    app = QApplication(sys.argv)
    gamee = Game_mama()
    gamee.show()
    sys.exit(app.exec_())

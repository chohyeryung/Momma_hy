import random
import sys

import pygame
from PyQt5.QtWidgets import *


class Game_hmama(QWidget):
    def __init__(self):
        super().__init__()
        pygame.init()  # 초기화 반드시 필요함
        self.initUI()

    def initUI(self):
        # 폰트
        clock = pygame.time.Clock()
        over_font = pygame.font.Font('babyb.ttf', 50)  # 폰트 ,크기
        small_font = pygame.font.Font('babyb.ttf', 36)
        missed = 0
        running = True
        clear = True
        BLUE = (8, 62, 163)
        # 총 시간
        total_time = 30
        screen_width = 480
        screen_height = 640
        screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 크기 설정
        clock = pygame.time.Clock()

        pygame.mixer.init()
        pygame.mixer.music.load('music/back_bgm.mp3') #배경 음악
        pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
        # missile_sound = pygame.mixer.Sound('missile.wav') #사운드
        # explosion_sound = pygame.mixer.Sound('explosion.wav')
        # game_over_sound = pygame.mixer.Sound('game_over.wav')

        bad_image = pygame.image.load("image/pepper.png")
        bads = []
        for i in range(3):
            bad = bad_image.get_rect(left=random.randint(0, screen_width - bad_image.get_width()), top=-100)
            dy = random.randint(3, 9)
            bads.append((bad, dy))

        bad2_image = pygame.image.load("image/donut.png")
        bads2 = []
        for i in range(3):
            bad2 = bad2_image.get_rect(left=random.randint(0, screen_width - bad2_image.get_width()), top=-100)
            dy = random.randint(3, 9)
            bads2.append((bad2, dy))

        bad3_image = pygame.image.load("image/cookie.png")
        bads3 = []
        for i in range(3):
            bad3 = bad3_image.get_rect(left=random.randint(0, screen_width - bad3_image.get_width()), top=-100)
            dy = random.randint(3, 9)
            bads3.append((bad3, dy))

        baby_image = pygame.image.load("image/game_baby.png")
        baby = baby_image.get_rect(centerx=screen_width // 2, bottom=screen_height)
        # 시작 시간 정보
        start_ticks = pygame.time.get_ticks()

        # 화면 타이틀 설정
        pygame.display.set_caption("아이에게 좋은것만 먹이세요")

        # 배경이미지 불러오기
        background = pygame.image.load("image/game_back.jpg")

        # running=True이면
        while running and clear:
            screen.blit(background, (0, 0))
            ellipsis_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 초 단위로 지난 시간 표시
            event = pygame.event.poll()  # 이벤트 처리
            if event.type == pygame.QUIT:
                break
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and not False:
                baby.left -= 7
            elif pressed[pygame.K_RIGHT] and not False:
                baby.left += 7

            for bad, dy in bads:
                bad.top += dy
                if bad.top > screen_height:
                    bads.remove((bad, dy))
                    bad = bad_image.get_rect(left=random.randint(0, screen_width - bad_image.get_width()),
                                             top=-100)
                    dy = random.randint(3, 9)
                    bads.append((bad, dy))
                    missed += 1

            for bad2, dy in bads2:
                bad2.top += dy
                if bad2.top > screen_height:
                    bads2.remove((bad2, dy))
                    bad2 = bad_image.get_rect(left=random.randint(0, screen_width - bad2_image.get_width()),
                                              top=-100)
                    dy = random.randint(3, 9)
                    bads2.append((bad2, dy))
                    missed += 1

            for bad3, dy in bads3:
                bad3.top += dy
                if bad3.top > screen_height:
                    bads3.remove((bad3, dy))
                    bad3 = bad_image.get_rect(left=random.randint(0, screen_width - bad3_image.get_width()),
                                              top=-100)
                    dy = random.randint(3, 9)
                    bads3.append((bad3, dy))
                    missed += 1

            if baby.left < 0:
                baby.left = 0
            elif baby.right > screen_width:
                baby.right = screen_width

            for bad, dy in bads:
                if bad.colliderect(baby):
                    # print('충돌')
                    # print(bad)
                    # print(fighter)
                    running = False

            for bad2, dy in bads2:
                if bad2.colliderect(baby):
                    # print('충돌')
                    # print(bad)
                    # print(fighter)
                    running = False

            for bad3, dy in bads3:
                if bad3.colliderect(baby):
                    # print('충돌')
                    # print(bad)
                    # print(fighter)
                    running = False

            for bad, dy in bads:
                screen.blit(bad_image, bad)

            for bad2, dy in bads2:
                screen.blit(bad2_image, bad2)

            for bad3, dy in bads3:
                screen.blit(bad3_image, bad3)

            # for good, dy in goods:
            #     screen.blit(good_image, good)

            screen.blit(baby_image, baby)

            timer = small_font.render("Time : {}".format(int(total_time - ellipsis_time)), True, (255, 255, 255))
            screen.blit(timer, (10, 20))
            missed_image = small_font.render('점수 {}'.format(missed), True, BLUE)
            screen.blit(missed_image, missed_image.get_rect(right=screen_width - 10, top=10))

            # 지정된 시간보다 시간을 초과한다면
            if total_time - ellipsis_time <= 0:
                running = False

            elif total_time == 0:
                running = False

            if running == False:
                pygame.mixer.music.stop()
                game_over_text = over_font.render('게임 종료', True, (255, 0, 0))
                game_over_score = over_font.render('점수 : {}'.format(missed), True, (255, 0, 0))
                screen.blit(game_over_text,
                            game_over_text.get_rect(centerx=screen_width // 2, centery=screen_height // 2 - 50))
                screen.blit(game_over_score,
                            game_over_score.get_rect(centerx=screen_width // 2, centery=screen_height // 2))

            if clear == False:
                pygame.mixer.music.stop()
                game_over_text = over_font.render('클리어', True, (255, 0, 0))
                game_over_score = over_font.render('점수 : {}'.format(missed), True, (255, 0, 0))
                screen.blit(game_over_text,
                            game_over_text.get_rect(centerx=screen_width // 2, centery=screen_height // 2 - 50))
                screen.blit(game_over_score,
                            game_over_score.get_rect(centerx=screen_width // 2, centery=screen_height // 2))

            pygame.display.update()  # 화면을 계속해서 호출해야 함
            clock.tick(60)

        pygame.time.delay(2000)
        pygame.quit()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main_":
    app = QApplication(sys.argv)
    hgamee = Game_hmama()
    hgamee.show()
    sys.exit(app.exec_())
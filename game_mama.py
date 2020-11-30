import pygame #파이 게임 모듈 임포트
import random
import sys
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication

class Game_mama(QWidget):
    def __init__(self):
        super().__init__()
        pygame.init() #초기화 반드시 필요함
        self.initUI()

    def initUI(self):
        pygame.init() #파이 게임 초기화
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 800
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
        clock = pygame.time.Clock()

        #변수

        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        large_font = pygame.font.SysFont('malgungothic', 72)
        small_font = pygame.font.SysFont('malgungothic', 36)
        score = 0
        missed = 0
        game_over = False

        background_image = pygame.image.load("image/back.png")
        rock_image = pygame.image.load("image/sandwich.png")
        rocks = []
        for i in range(3):
            rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
            dy = random.randint(3, 9)
            rocks.append((rock, dy))

        missile_image = pygame.image.load("image/bottle.png")
        missiles = []

        explosion_image = pygame.image.load("image/atack.png")

        fighter_image = pygame.image.load("image/game_baby.png")
        fighter = fighter_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT)

            # pygame.mixer.init()
            # pygame.mixer.music.load('music.mid') #배경 음악
            # pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
            # missile_sound = pygame.mixer.Sound('missile.wav') #사운드
            # explosion_sound = pygame.mixer.Sound('explosion.wav')
            # game_over_sound = pygame.mixer.Sound('game_over.wav')

        while True: #게임 루프
            screen.blit(background_image, (0, 0))

                #변수 업데이트

            event = pygame.event.poll() #이벤트 처리
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_SPACE:
                    missile = missile_image.get_rect(centerx=fighter.centerx, top=fighter.top)
                    missiles.append(missile)

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT] and not game_over:
                fighter.left -= 5
            elif pressed[pygame.K_RIGHT] and not game_over:
                fighter.left += 5

            if not game_over:
                for rock, dy in rocks:
                    rock.top += dy
                    if rock.top > SCREEN_HEIGHT:
                        rocks.remove((rock, dy))
                        rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                        dy = random.randint(3, 9)
                        rocks.append((rock, dy))
                        missed += 1

                if missed >= 100:
                    game_over = True
                    pygame.mixer.music.stop()

                for missile in missiles:
                    missile.top -= 6
                    if missile.top < 0:
                        missiles.remove(missile)

                if fighter.left < 0:
                    fighter.left = 0
                elif fighter.right > SCREEN_WIDTH:
                    fighter.right = SCREEN_WIDTH

                for rock, dy in rocks:
                    for missile in missiles:
                        if missile.colliderect(rock):
                            rocks.remove((rock, dy))
                            missiles.remove(missile)
                            screen.blit(explosion_image, (rock.left, rock.top))
                            rock = rock_image.get_rect(left=random.randint(0, SCREEN_WIDTH - rock_image.get_width()), top=-100)
                            dy = random.randint(3, 9)
                            rocks.append((rock, dy))
                            score += 1

                for rock, dy in rocks:
                    if rock.colliderect(fighter):
                        game_over = True
                        pygame.mixer.music.stop()

                #화면 그리기

            for rock, dy in rocks:
                    screen.blit(rock_image, rock)

            for missile in missiles:
                    screen.blit(missile_image, missile)

            screen.blit(fighter_image, fighter)

            score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
            screen.blit(score_image, (10, 10))

            missed_image = small_font.render('놓친 운석 수 {}'.format(missed), True, YELLOW)
            screen.blit(missed_image, missed_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

            if (game_over == False):
                print('good')
                game_over_image = large_font.render('게임 종료', True, (255, 0, 0))
                screen.blit(game_over_image, (75, 200))

            pygame.display.update() #모든 화면 그리기 업데이트
            clock.tick(60) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

    pygame.time.delay(2000)
    pygame.quit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    gamee = Game_mama()
    gamee.show()
    sys.exit(app.exec_())
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

        #폰트
        game_font = pygame.font.Font(None, 40) #폰트 ,크기

        #총 시간
        total_time = 15

        large_font = pygame.font.SysFont('malgungothic', 72)

        #닿은 횟수
        count = 0

        # 총 점수
        total_score = 100
        #시작 시간 정보
        start_ticks = pygame.time.get_ticks()

        #창크기
        screen_width = 480
        screen_height = 640

        screen = pygame.display.set_mode((screen_width, screen_height))

        #화면 타이틀 설정
        pygame.display.set_caption("아이에게 좋은것만 먹이세요")

        #초당 프레임
        clock = pygame.time.Clock()

        #배경이미지 불러오기
        background = pygame.image.load("image/game_back.jpg")

        #캐릭터 불러오기
        character= pygame.image.load("image/game_baby.png")
        character_size = character.get_rect().size # 이미지 크기 구해옴 70*70 적당함
        character_width = character_size[0] #가로크기
        character_height = character_size[1] #세로 크기
        character_x_pos = (screen_width / 2) -  (character_width / 2)#중앙에 배치
        character_y_pos = screen_height - character_height # 가장 아래

        #이동 좌표
        to_x = 0

        #캐릭터 이동 속도
        character_speed = 9

        #나쁜 음식
        enemy1 = pygame.image.load("image/sandwich.png")
        enemy1_size = enemy1.get_rect().size  # 이미지 크기 구해옴 70*70 적당함
        enemy1_width = enemy1_size[0]  # 가로크기
        enemy1_height = enemy1_size[1]  # 세로 크기
        enemy_x_pos1 = random.randint(0, screen_width - enemy1_width)
        enemy_y_pos1 = 0
        enemy_speed = 7

        enemy2 = pygame.image.load("image/honey.png")
        enemy2_size = enemy2.get_rect().size  # 이미지 크기 구해옴 70*70 적당함
        enemy2_width = enemy2_size[0]  # 가로크기
        enemy2_height = enemy2_size[1]  # 세로 크기
        enemy_x_pos2 = random.randint(0, screen_width - enemy2_width)
        enemy_y_pos2 = 0
        enemy_speed = 7

        good = pygame.image.load("image/apple.png")
        good_size = good.get_rect().size  # 이미지 크기 구해옴 70*70 적당함
        good_width = good_size[0]  # 가로크기
        good_height = good_size[1]  # 세로 크기
        goody_x_pos3 = random.randint(0, screen_width - good_width)
        goody_y_pos3 = 0
        enemy_speed = 7

        print(enemy_x_pos1)
        print(enemy_x_pos2)
        print(goody_x_pos3)

        #이벤트 루프 없으면 창 바로 꺼짐
        running = True
        while running:
            dt = clock.tick(60)
            print("fps : " + str(clock.get_fps()))

            for event in pygame.event.get(): #어떤 이벤트가 발생하였는지
                if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 실행되었는지
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_x -= character_speed
                    elif event.key == pygame.K_RIGHT:
                        to_x += character_speed

                if event.type == pygame.KEYUP: # 키보드에서 손을 땠을 시
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        to_x = 0

            character_x_pos += to_x

            #캐릭터 위치
            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

            enemy_y_pos1 += enemy_speed
            enemy_y_pos2 += enemy_speed
            goody_y_pos3 += enemy_speed

            if enemy_y_pos1 > screen_height:
                enemy_y_pos1 = 0
                enemy_x_pos1 = random.randint(0, screen_width - enemy1_width)
                enemy_y_pos1 > screen_height
                enemy_y_pos1 = 0
                enemy_x_pos1 = random.randint(0, screen_width - enemy1_width)

            if enemy_y_pos2 > screen_height:
                enemy_y_pos2 = 0
                enemy_x_pos2 = random.randint(0, screen_width - enemy2_width)
                enemy_y_pos2 > screen_height
                enemy_y_pos2 = 0
                enemy_x_pos2 = random.randint(0, screen_width - enemy2_width)

            if goody_y_pos3 > screen_height:
                goody_y_pos3 = 0
                goody_x_pos3 = random.randint(0, screen_width - good_width)
                goody_y_pos3 > screen_height
                goody_y_pos3 = 0
                goody_x_pos3 = random.randint(0, screen_width - good_width)

            #충돌 처리
            character_reat = character.get_rect()
            character_reat.left = character_x_pos
            character_reat.top = character_y_pos

            enemy1_reat = enemy1.get_rect()
            enemy1_reat.left = enemy_x_pos1
            enemy1_reat.top = enemy_y_pos1

            enemy2_reat = enemy2.get_rect()
            enemy2_reat.left = enemy_x_pos2
            enemy2_reat.top = enemy_y_pos2

            good_reat = good.get_rect()
            good_reat.left = goody_x_pos3
            good_reat.top = goody_y_pos3


            #충돌 체크
            if character_reat.colliderect(enemy1_reat):
                count += 1
                print(count)
                print("나쁜 음식을 먹었습니다!")
                total_score -= 10
                running = True


            elif character_reat.colliderect(enemy2_reat):
                count += 1
                print(count)
                print("나쁜 음식을 먹었습니다!")
                total_score -= 10
                running = True

            elif character_reat.colliderect(good_reat):
                count += 1
                print(count)
                print("좋은 음식을 먹었습니다!")
                total_score += 10
                running = True

            # screen.fill(()) RGB컬러로도 화면 채우기 가능
            screen.blit(background, (0,0))
            screen.blit(character, (character_x_pos, character_y_pos))#캐릭터 그리기
            screen.blit(enemy1, (enemy_x_pos1, enemy_y_pos1)) #나쁜 음식 그리기
            screen.blit(enemy2, (enemy_x_pos2, enemy_y_pos2)) #나쁜 음식 그리기
            screen.blit(good, (goody_x_pos3, goody_y_pos3)) #좋은 음식 그리기

            ellipsis_time = (pygame.time.get_ticks() - start_ticks) / 1000 #초 단위로 지난 시간 표시

            #출력할 글자 ,True, 글자 색 설정
            timer= game_font.render("Time : {}".format(int(total_time - ellipsis_time)), True, (255,255,255))
            screen.blit(timer, (10, 20))
            Total_score_show = game_font.render("Score : {}".format(total_score), True, (255, 255, 255))
            screen.blit(Total_score_show, (140, 20))

            healthvalue = 100

            health_bar = pygame.image.load("image/healt.png")
            health = pygame.image.load("image/healt_minus.png")

            screen.blit(health_bar, (5, 5))
            for health1 in range(healthvalue):
                screen.blit(health, (health1 + 3, 3))

            #지정된 시간보다 시간을 초과한다면
            if total_time - ellipsis_time <= 0:
                running=False

            elif total_time==0:
                running = False

            elif total_score==0:
                running = False

            elif healthvalue <= 0:
                running = False

            if (running == False):
                print('good')
                game_over_image = large_font.render('게임 종료', True, (255, 0, 0))
                screen.blit(game_over_image, (75, 200))

            pygame.display.update()  # 화면을 계속해서 호출해야 함

        pygame.time.delay(2000)
        pygame.quit()

    def closeEvent(self, event):
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
import random
import sys

import pygame
from PyQt5.QtWidgets import *

class Game_mama(QWidget):

    def __init__(self, choice_window):
        pygame.init() #초기화 반드시 필요함
        self.choice_window=choice_window
        self.initUI()

    def initUI(self):

        #폰트
        game_font = pygame.font.Font(None, 40) #폰트 ,크기

        #총 시간
        total_time = 15

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

        #이미지 랜덤
        bad1 = pygame.image.load("image/coffee.png")
        bad2 = pygame.image.load("image/honey.png")
        bad3 = pygame.image.load("image/raman.png")
        bad4 = pygame.image.load("image/spicy.JPG")

        bad_image = [bad1, bad2, bad3, bad4]
        #
        # random_img = random.randint(0, bad_image.length())

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

        enemy3 = pygame.image.load("image/apple.png")
        enemy3_size = enemy3.get_rect().size  # 이미지 크기 구해옴 70*70 적당함
        enemy3_width = enemy3_size[0]  # 가로크기
        enemy3_height = enemy3_size[1]  # 세로 크기
        enemy_x_pos3 = random.randint(0, screen_width - enemy3_width)
        enemy_y_pos3 = 0
        enemy_speed = 7

        print(enemy_x_pos1)
        print(enemy_x_pos2)
        print(enemy_x_pos3)

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
            enemy_y_pos3 += enemy_speed

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

            if enemy_y_pos3 > screen_height:
                enemy_y_pos3 = 0
                enemy_x_pos3 = random.randint(0, screen_width - enemy3_width)
                enemy_y_pos3 > screen_height
                enemy_y_pos3 = 0
                enemy_x_pos3 = random.randint(0, screen_width - enemy3_width)

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

            enemy3_reat = enemy3.get_rect()
            enemy3_reat.left = enemy_x_pos3
            enemy3_reat.top = enemy_y_pos3


            #충돌 체크
            if character_reat.colliderect(enemy1_reat):
                count += 1
                print(count)
                print("나쁜 음식을 먹었습니다!")
                if count < 2:
                    total_score -= 50
                    running = True

            elif character_reat.colliderect(enemy2_reat):
                count += 1
                print(count)
                print("나쁜 음식을 먹었습니다!")
                if count < 2:
                    total_score -= 50
                    running = True


            elif character_reat.colliderect(enemy3_reat):
                count += 1
                print(count)
                print("좋은 음식을 먹었습니다!")
                if count < 2:
                    total_score +=50
                    running = True


            # screen.fill(()) RGB컬러로도 화면 채우기 가능
            screen.blit(background, (0,0))
            screen.blit(character, (character_x_pos, character_y_pos))#캐릭터 그리기
            screen.blit(enemy1, (enemy_x_pos1, enemy_y_pos1)) #적 그리기
            screen.blit(enemy2, (enemy_x_pos2, enemy_y_pos2)) #적 그리기
            screen.blit(enemy3, (enemy_x_pos3, enemy_y_pos3)) #적 그리기

            ellipsis_time = (pygame.time.get_ticks() - start_ticks) / 1000 #초 단위로 지난 시간 표시

            #출력할 글자 ,True, 글자 색 설정
            timer= game_font.render("Time : {}".format(int(total_time - ellipsis_time)), True, (255,255,255))
            screen.blit(timer, (10, 20))
            Total_score_show = game_font.render("Score : {}".format(total_score), True, (255, 255, 255))
            screen.blit(Total_score_show, (140, 20))

            #지정된 시간보다 시간을 초과한다면
            if total_time - ellipsis_time <= 0:
                running = False

            elif total_time==0:
                running=False

            elif total_score==0:
                running=False

            pygame.display.update()  # 화면을 계속해서 호출해야 함

        #끝나기 전 잠시 기달리는 시간
        pygame.time.delay(3000)

        #py게임 종료
        self.choice_window.show()
        pygame.quit()


if __name__=="__main__":
    app = QApplication(sys.argv)
    gamee = Game_mama()
    gamee.show()
    sys.exit(app.exec_())
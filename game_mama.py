import random
import sys

import pygame
from PyQt5.QtWidgets import *

class Game_mama(QWidget):

    def __init__(self):
        pygame.init() #초기화 반드시 필요함
        self.initUI()

    def initUI(self):

        #폰트
        game_font = pygame.font.Font(None, 40) #폰트 ,크기

        #총 시간
        total_time = 15

        #닿은 횟수
        count = 0

        # 총 점수
        total_score = 0
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

        # bad_image = [bad1, bad2, bad3, bad4]
        #
        # random_img = random.randint(0, bad_image.length())

        #캐릭터 이동 속도
        character_speed = 9

        #나쁜 음식
        enemy = pygame.image.load("image/sandwich.png")
        enemy_size = enemy.get_rect().size  # 이미지 크기 구해옴 70*70 적당함
        enemy_width = enemy_size[0]  # 가로크기
        enemy_height = enemy_size[1]  # 세로 크기
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        enemy_speed = 7

        #좋은 캐릭터
        goodfood = pygame.image.load("image/good.png")
        goodfood_size = goodfood.get_rect().size
        goodfood_width = goodfood_size[0]
        goodfood_height = goodfood_size[1]
        goodfood_x_pos = random.randint(0, screen_width - goodfood_width)
        goodfood_y_pos = 0
        goodfood_speed = 7

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

            enemy_y_pos += enemy_speed

            if enemy_y_pos > screen_height:
                enemy_y_pos = 0
                enemy_x_pos = random.randint(0, screen_width - enemy_width)
                enemy_y_pos > screen_height
                enemy_y_pos = 0
                enemy_x_pos = random.randint(0, screen_width - enemy_width)

            #충돌 처리
            character_reat = character.get_rect()
            character_reat.left = character_x_pos
            character_reat.top = character_y_pos

            enemy_reat = enemy.get_rect()
            enemy_reat.left = enemy_x_pos
            enemy_reat.top = enemy_y_pos

            #충돌 체크
            if character_reat.colliderect(enemy_reat):
                count += 1
                print(count)
                print("나쁜 음식을 먹었습니다!")
                total_score = total_score - 5
                running = False


            # screen.fill(()) RGB컬러로도 화면 채우기 가능
            screen.blit(background, (0,0))
            screen.blit(character, (character_x_pos, character_y_pos))#캐릭터 그리기
            screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 그리기

            ellipsis_time = (pygame.time.get_ticks() - start_ticks) / 1000 #초 단위로 지난 시간 표시

            #출력할 글자 ,True, 글자 색 설정
            timer= game_font.render("Time : {}".format(int(total_time - ellipsis_time)), True, (255,255,255))
            screen.blit(timer, (10, 20))

            #지정된 시간보다 시간을 초과한다면
            if total_time - ellipsis_time <= 0:
                running = False

            pygame.display.update()  # 화면을 계속해서 호출해야 함

        #끝나기 전 잠시 기달리는 시간
        pygame.time.delay(3000)

        #py게임 종료
        pygame.quit()

if __name__=="__main__":
    app = QApplication(sys.argv)
    gamee = Game_mama()
    gamee.show()
    sys.exit(app.exec_())
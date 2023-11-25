import pygame
from paddle import *
from ball import *
from function import draw,handle_collision,handle_paddle_movement

pygame.init()

FPS = 60
paused=False

WIDTH, HEIGHT = 700, 500
WHITE = (0, 0, 0)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10

def main():
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Pong")
    scene = "scene_menu"
    while True:
        if scene == "scene_menu":
            scene = menu(screen)
        elif scene == "scene_game":
            scene = pong(screen)
        else:
            break

def menu_display(screen,menu_pong,menu_key):
    screen.fill((192, 192, 192))
    screen.blit(menu_pong, (screen.get_width() / 2 - menu_pong.get_width() / 2, screen.get_height() / 4 - menu_pong.get_height() / 2))
    screen.blit(menu_key, (screen.get_width() / 2 - menu_key.get_width() / 2, screen.get_height() / 2 + menu_key.get_height() / 2))

    triangle_vertices = [(screen.get_width() / 2, screen.get_height() / 2 + 90),(screen.get_width() / 2 - 40, screen.get_height() / 2 + 130),
                         (screen.get_width() / 2 + 40, screen.get_height() / 2 + 130)]

    pygame.draw.polygon(screen, (40, 40, 40), triangle_vertices)
    pygame.display.update()

def menu_handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            scene = "scene_game"
            return scene

def menu(screen):
    txt_font = pygame.font.Font('8-BIT WONDER.ttf', 45)
    txt_font2=pygame.font.Font('8-BIT WONDER.ttf', 25)
    menu_pong = txt_font.render("PONG GAME", False, (40, 40, 40))
    menu_key = txt_font2.render("Press any key to begin", False, (40, 40, 40))

    menu_display(screen, menu_pong, menu_key)

    while True:
        scene = menu_handle_menu_events()
        if scene:
            return scene

def pong_paused(WIN,ball,txt_font,txt_font2):
    txt = txt_font.render("PAUSED", False, (225, 225, 225))
    WIN.blit(txt, (WIN.get_width() / 2 - txt.get_width() / 2, WIN.get_height() / 4 - txt.get_height() / 2))

    tx2 = txt_font2.render("Current ball speed is " + (str)(ball.get_speed()), False, (225, 225, 225))
    tx3 = txt_font2.render("To increase the speed press the 1 button ", False, (225, 225, 225))
    tx4 = txt_font2.render("and to decrease it press the 2 button on the keyboard (q to quit)", False, (225, 225, 225))

    WIN.blit(tx2, (WIN.get_width() / 2 - tx2.get_width() / 2, WIN.get_height() / 2 + tx2.get_height()))
    WIN.blit(tx3, (WIN.get_width() / 2 - tx3.get_width() / 2,WIN.get_height() / 2 + tx3.get_height() + 30))
    WIN.blit(tx4, (WIN.get_width() / 2 - tx4.get_width() / 2,WIN.get_height() / 2 + tx4.get_height() + 60))

    pygame.display.update()

def pong(WIN):
    txt_font = pygame.font.Font('8-BIT WONDER.ttf', 45)
    txt_font2 = pygame.font.Font('8-BIT WONDER.ttf', 11)
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT //2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("SPACE key pressed")
                    global paused
                    paused=not paused
                if (paused):
                    keys = pygame.key.get_pressed()  # Get the currently pressed keys
                    if keys[pygame.K_1]:
                        ball.speed_increment()
                    elif keys[pygame.K_2]:
                        ball.speed_decrement()
                    elif keys[pygame.K_q]:
                        run = False
                        break
                    pygame.display.update()


        if paused:
            pong_paused(WIN,ball,txt_font,txt_font2)

        if not paused:
            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > WIDTH:
                left_score += 1
                ball.reset()

            won = False
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = SCORE_FONT.render(win_text, 1, WHITE)
                WIN.blit(text, (WIDTH // 2 - text.get_width() //
                                2, HEIGHT // 2 - text.get_height() // 2))
                pygame.display.update()
                pygame.time.delay(5000)
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                left_score = 0
                right_score = 0

    pygame.quit()

if __name__ == "__main__":
    main()
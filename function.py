import pygame

pygame.init()
WIDTH, HEIGHT = 700, 500
WHITE = (0, 0, 0)
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

def draw_scores(win, left_score, right_score):
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

def draw_background(win):
    win.fill((192, 192, 192))
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

def draw_game_elements(win, paddles, ball):
    for paddle in paddles:
        paddle.draw(win)
    ball.draw(win)

def draw(win, paddles, ball, left_score, right_score):
    draw_background(win)
    draw_scores(win,left_score,right_score)
    draw_game_elements(win,paddles,ball)
    pygame.display.update()


def handle_vertical_collision(ball):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

def handle_left_paddle_collision(ball, left_paddle):
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.speed_ball
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

def handle_right_paddle_collision(ball, right_paddle):
    if ball.x_vel > 0:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.speed_ball
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

def handle_collision(ball, left_paddle, right_paddle):
    handle_vertical_collision(ball)
    handle_left_paddle_collision(ball, left_paddle)
    handle_right_paddle_collision(ball, right_paddle)

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.vel >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.vel + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.vel >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.vel + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)
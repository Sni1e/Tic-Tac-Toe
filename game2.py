import pygame
import random

pygame.init()

WIDTH = 300
HEIGHT = 300
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
field = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]


def draw_grid():
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 3)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 3)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 3)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 3)


def draw_x_0():
    for x in range(3):
        for y in range(3):
            if field[x][y] == 'x':
                pygame.draw.line(screen, BLACK, (y * 100 + 5, x * 100 + 5), (y * 100 + 95, x * 100 + 95), 3)
                pygame.draw.line(screen, BLACK, (y * 100 + 95, x * 100 + 5), (y * 100 + 5, x * 100 + 95), 3)
            elif field[x][y] == '0':
                pygame.draw.circle(screen, BLACK, (y * 100 + 50, x * 100 + 50), 40, 3)


# noinspection PyGlobalUndefined

def win_check(symbol):
    flag_win = False
    global win
    for x in field:
        if x.count(symbol) == 3:
            flag_win = True
            win = [[0, field.index(x)], [1, field.index(x)], [2, field.index(x)]]

    for y in range(3):
        if field[0][y] == field[1][y] == field[2][y] == symbol:
            flag_win = True
            win = [[y, 0], [y, 1], [y, 2]]
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        flag_win = True
        win = [[0, 2], [1, 1], [2, 0]]

    return flag_win


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')

clock = pygame.time.Clock()
run_game = True

game_over = False

while run_game:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_position = pygame.mouse.get_pos()
            if field[mouse_position[1] // 100][mouse_position[0] // 100] == '':
                field[mouse_position[1] // 100][mouse_position[0] // 100] = 'x'
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                while field[x][y] != '':
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                field[x][y] = '0'
        elements = \
            field[0].count('x') + \
            field[0].count('0') + \
            field[1].count('x') + \
            field[1].count('0') + \
            field[2].count('x') + \
            field[2].count('0')
        player = win_check('x')
        ai = win_check('0')
        if player or ai:
            game_over = True
            if player:
                pygame.display.set_caption('Вы победили!')
            elif ai:
                pygame.display.set_caption('Вы проиграли!')
        elif elements == 8:
            pygame.display.set_caption('Ничья')
    if game_over:
        pygame.draw.rect(screen, GREEN, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(screen, GREEN, (win[2][0] * 100, win[2][1] * 100, 100, 100))

    draw_x_0()
    draw_grid()
    pygame.display.flip()

pygame.quit()
quit()

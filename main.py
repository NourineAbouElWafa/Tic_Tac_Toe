import numpy as np
import pygame,sys

pygame.init()
WIDTH=600
HEIGHT=600
ROWS=3
COLUMNS=3
BG_COLOR=pygame.Color('#9CB4CC')
LINE_COLOR=pygame.Color('#748DA6')
CIRCLE_COLOR=pygame.Color('#F0EBE3')
CROSS_COLOR=pygame.Color('#3F4E4F')
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
#setting screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC-TAC-TOE")
screen.fill(BG_COLOR)
#drawing lines
pygame.draw.line(screen,LINE_COLOR,(0,SQUARE_SIZE),(SQUARE_SIZE*3,SQUARE_SIZE),10)
pygame.draw.line(screen,LINE_COLOR,(0,SQUARE_SIZE*2),(SQUARE_SIZE*3,SQUARE_SIZE*2),10)
pygame.draw.line(screen,LINE_COLOR,(SQUARE_SIZE,0),(SQUARE_SIZE,SQUARE_SIZE*3),10)
pygame.draw.line(screen,LINE_COLOR,(SQUARE_SIZE*2,0),(SQUARE_SIZE*2,SQUARE_SIZE*3),10)

#setting board to check for later

board=np.zeros((ROWS,COLUMNS))

#functions for the game



def draw_figures():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE/2), int(row * SQUARE_SIZE + SQUARE_SIZE/2)), CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]==2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


def claim_square(row,col,player):
    board[row][col]=player


def is_availble(row,col):
    return board[row][col]==0


def is_full():
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col]==0:
                return False
    return True


def check_winner(player):
    # vertical win check
    for col in range(COLUMNS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # asc diagonal win check
    if board[0][0]==player and board[1][1]==player and board[2,2]==player:
        draw_desc_diagonal(player)
        return True


def draw_vertical_winning_line(col, player):
    posX=col*SQUARE_SIZE+SQUARE_SIZE/2
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 10)



def draw_horizontal_winning_line(row, player):
    posY=row*SQUARE_SIZE+SQUARE_SIZE/2
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), 10)


def draw_asc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 10)


def draw_desc_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 10)


def restart():
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SQUARE_SIZE * 3, SQUARE_SIZE), 10)
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * 2), (SQUARE_SIZE * 3, SQUARE_SIZE * 2), 10)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE * 3), 10)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, SQUARE_SIZE * 3), 10)
    for row in range(ROWS):
        for col in range(COLUMNS):
            board[row][col]=0




play=1
game_over=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            X=event.pos[0]
            Y=event.pos[1]

            clicked_row=int(Y//SQUARE_SIZE)
            clicked_col=int(X//SQUARE_SIZE)
            if is_availble(clicked_row,clicked_col):
                if play==1:
                    claim_square(clicked_row,clicked_col,1)
                    if check_winner(play):
                        game_over=True
                    play=2

                elif play==2:
                    claim_square(clicked_row,clicked_col,2)
                    if check_winner(play):
                        game_over=True
                    play=1

                draw_figures()
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    restart()
                    play = 1
                    game_over = False
    pygame.display.update()
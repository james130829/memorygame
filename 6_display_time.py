import pygame
from random import *

def setup(level):
    number_count = (level // 2) * 2 + 4
    number_count = min(number_count, 16)

    shuffle_gride(number_count)

def shuffle_gride(number_count):
    rows =7
    columns = 13

    grid = [[0 for c in range(columns)]for r in range(rows)]

    number = 1

    while number <= number_count:
        row_idx = randrange(0,rows)
        column_idx = randrange(0,columns)
        if grid[row_idx][column_idx] == 0:
            grid[row_idx][column_idx] = number
            number +=1

            center_x = column_idx * 100 + 50
            center_y = row_idx * 100 +50

            button = pygame.Rect(0,0,90,90)
            button.center = (center_x, center_y)

            number_buttons.append(button)

    print(grid)

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 70, 5)

def display_game_screen():
    screen.fill(BLACK)
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            pygame.draw.rect(screen,GRAY,rect)
        else:
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)
def check_button(pos):
    global start,start_ticks
    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global hidden
    
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")

                del number_buttons[0]

                if not hidden:
                    hidden = True
            else:
                print("Wrong")

pygame.init()
screen_width = 1300
screen_height = 700

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50,50,50)

display_time = 5
start_ticks = None

game_font = pygame.font.Font(None, 120)

number_buttons = []

screen = pygame.display.set_mode((screen_width,screen_height))

start_button = pygame.Rect(0, 0, 140, 140)
start_button.center = (140, screen_height - 140)

start = False

hidden = False

setup(1)

running = True

while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()

    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()
    
    if click_pos:
        check_button(click_pos)

    pygame.display.update()

pygame.quit()
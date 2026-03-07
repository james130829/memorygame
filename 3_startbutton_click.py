import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 70, 5)
pygame.init()
def display_game_screen():
    print("게임화면")
def check_button(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

screen_width = 1280
screen_height = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((screen_width,screen_height))

start_button = pygame.Rect(0, 0, 140, 140)
start_button.center = (140, screen_height - 140)

start = False

running = True

while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        display_start_screen()
    
    if click_pos:
        check_button(click_pos)

    display_start_screen()

    pygame.display.update()

pygame.quit()
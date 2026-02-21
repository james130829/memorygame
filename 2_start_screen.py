import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 70, 5)
pygame.init()

screen_width = 1280
screen_height = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((screen_width,screen_height))

start_button = pygame.Rect(0, 0, 140, 140)
start_button.center = (140, screen_height - 140)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    display_start_screen()

    pygame.display.update()

pygame.quit()
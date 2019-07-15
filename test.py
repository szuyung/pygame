import pygame
import time

pygame.init()
display_width = 800
display_height = 600
gameScreen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('貪吃蛇')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

lead_x = display_width / 2
lead_y = display_height / 2
lead_x_change = 0
lead_y_change = 0
size_of_block = 10
clock = pygame.time.Clock()
fps = 15


def msg_to_screen(msg, type):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, type)
    gameScreen.blit(screen_text, [display_width/2, display_height/2])





gameRun = True
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -size_of_block
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = size_of_block
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -size_of_block
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = size_of_block
                lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x >= display_width or lead_x < size_of_block or lead_y >= display_height or lead_y < 0:
            gameRun = False

    gameScreen.fill(white)
    pygame.draw.rect(gameScreen, black, (lead_x, lead_y, 10, 10))
    pygame.display.update()
    clock.tick(fps)

msg_to_screen("You lose", red)
pygame.display.update()
time.sleep(2)

pygame.quit()

quit()

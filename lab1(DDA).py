import pygame

import sys

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("DDA Line Drawing Algorithm") 

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

def draw_line(x1, y1, x2, y2, thickness):

    dx = x2 - x1

    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps

    y_inc = dy / steps

    x = x1

    y = y1

    for i in range(steps):

        pygame.draw.circle(screen, WHITE, (round(x), round(y)), thickness // 2)

        x += x_inc

        y += y_inc

def main():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

        screen.fill(BLACK)

        draw_line(20, 20, 100, 100, 5) # Increase thickness to 5 pixels

        pygame.display.flip()

if __name__ == "__main__":

    main()

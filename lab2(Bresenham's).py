import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("Bresenham's Line Algorithm") 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line(x1, y1, x2, y2, thickness):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    pygame.draw.circle(screen, WHITE, (x, y), thickness // 2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_line(50, 50, 10, 100, 3)  
        draw_line(50, 50, 100, 100, 3)  
        draw_line(10, 100, 100, 100, 3) 
        draw_line(10, 70, 100, 70, 3) 
        draw_line(10, 70, 50, 120, 3) 
        draw_line(100, 70, 50, 120, 3) 
        
        pygame.display.flip()

if __name__ == "__main__":
    main()

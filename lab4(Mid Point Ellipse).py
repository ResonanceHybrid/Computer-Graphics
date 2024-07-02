import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ellipse Drawing Algorithm")

GOLD = (255, 215, 0)
WHITE = (0, 0, 0)

def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    rx_sq = rx ** 2
    ry_sq = ry ** 2
    tworx_sq = 2 * rx_sq
    twory_sq = 2 * ry_sq
    px = 0
    py = tworx_sq * y

    # Initial decision parameter for region 1
    p1 = ry_sq - (rx_sq * ry) + (0.25 * rx_sq)
    while px < py:
        screen.set_at((xc + x, yc + y), GOLD)
        screen.set_at((xc - x, yc + y), GOLD)
        screen.set_at((xc + x, yc - y), GOLD)
        screen.set_at((xc - x, yc - y), GOLD)

        x += 1
        px += twory_sq
        if p1 < 0:
            p1 += ry_sq + px
        else:
            y -= 1
            py -= tworx_sq
            p1 += ry_sq + px - py

    # Initial decision parameter for region 2
    p2 = (ry_sq) * ((x + 0.5) ** 2) + (rx_sq) * ((y - 1) ** 2) - (rx_sq * ry_sq)
    while y > 0:
        screen.set_at((xc + x, yc + y), GOLD)
        screen.set_at((xc - x, yc + y), GOLD)
        screen.set_at((xc + x, yc - y), GOLD)
        screen.set_at((xc - x, yc - y), GOLD)

        y -= 1
        py -= tworx_sq
        if p2 > 0:
            p2 += rx_sq - py
        else:
            x += 1
            px += twory_sq
            p2 += rx_sq - py + px

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)

        # Draw the ellipse
        draw_ellipse(WIDTH // 2, HEIGHT // 2, 200, 100)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

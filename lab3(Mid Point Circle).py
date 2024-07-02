import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 800
white = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_position = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, white, circle_position, 50)

    pygame.display.flip()

pygame.quit()

import pygame
import math


pygame.init()


WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))


sun_position = (WIDTH // 2, HEIGHT // 2)
planet_positions = [
    (WIDTH // 2 + 100, HEIGHT // 2, math.radians(0)),  
    (WIDTH // 2 + 200, HEIGHT // 2, math.radians(0)),  
    (WIDTH // 2 + 300, HEIGHT // 2, math.radians(0)), 
    (WIDTH // 2 + 400, HEIGHT // 2, math.radians(0))   
]


planet_speeds = [0.001, 0.0015, 0.002, 0.0025]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill((0, 0, 0))

   
    pygame.draw.circle(screen, YELLOW, sun_position, 50)

   
    for i, (x, y, angle) in enumerate(planet_positions):
        radius = 100 * (i + 1)  
        angle += planet_speeds[i]  
        x = sun_position[0] + int(radius * math.cos(angle))
        y = sun_position[1] + int(radius * math.sin(angle))
        planet_positions[i] = (x, y, angle)
        if i == 0:
            pygame.draw.circle(screen, BLUE, (x, y), 20)
        elif i == 1:
            pygame.draw.circle(screen, GREEN, (x, y), 15)
        elif i == 2:
            pygame.draw.circle(screen, ORANGE, (x, y), 10)
        elif i == 3:
            pygame.draw.circle(screen, RED, (x, y), 15)

   
    for i in range(4):
        pygame.draw.circle(screen, WHITE, sun_position, 100 * (i + 1), 1)

  
    pygame.display.flip()


pygame.quit()

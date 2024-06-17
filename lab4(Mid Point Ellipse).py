import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define planet parameters (radius, distance from sun, speed, color)
planets = [
    {"radius": 10, "distance": 100, "speed": 0.01, "color": BLUE},
    {"radius": 15, "distance": 150, "speed": 0.008, "color": RED},
    {"radius": 20, "distance": 200, "speed": 0.005, "color": GREEN}
]

def draw_planet(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Background color

    # Draw Sun
    pygame.draw.circle(screen, YELLOW, (400, 300), 30)

    # Draw planets
    for planet in planets:
        # Calculate planet position based on its distance and angle
        angle = pygame.time.get_ticks() * planet["speed"]
        x = int(400 + planet["distance"] * math.cos(angle))
        y = int(300 + planet["distance"] * math.sin(angle))
        draw_planet(x, y, planet["radius"], planet["color"])

    pygame.display.update()

pygame.quit()
sys.exit()
 
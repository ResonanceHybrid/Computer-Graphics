import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Transformations: Translation, Scaling, Rotation")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw_line(screen, color, x1, y1, x2, y2, thickness=1):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), thickness)

def translate(x, y, tx, ty):
    return x + tx, y + ty

def scale(x, y, sx, sy):
    return int(x * sx), int(y * sy)

def rotate_point(point, angle, origin):
    ox, oy = origin
    px, py = point
    angle_rad = math.radians(angle)
    qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
    qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
    return round(qx), round(qy)

def draw_transformed_line(x1, y1, x2, y2, thickness, color=WHITE, tx=0, ty=0, sx=1.0, sy=1.0, angle=0):
    # Apply translation
    x1, y1 = translate(x1, y1, tx, ty)
    x2, y2 = translate(x2, y2, tx, ty)
    
    # Apply scaling
    x1, y1 = scale(x1, y1, sx, sy)
    x2, y2 = scale(x2, y2, sx, sy)
    
    # Rotate endpoints around (x1, y1)
    rotated_start = rotate_point((x1, y1), angle, (x1, y1))
    rotated_end = rotate_point((x2, y2), angle, (x1, y1))

    draw_line(screen, color, rotated_start[0], rotated_start[1], rotated_end[0], rotated_end[1], thickness)

def main():
    print("Enter Translation Coordinates")
    number_tx = int(input("Enter a number tx: "))
    number_ty = int(input("Enter a number ty: "))

    print("Enter Scaling Factors")
    sx = float(input("Enter a scaling factor sx: "))
    sy = float(input("Enter a scaling factor sy: "))

    print("Enter Rotation Angle (in degrees)")
    angle = float(input("Enter rotation angle: "))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Original line
        draw_line(screen, WHITE, 50, 50, 100, 100, 3)

        # Translated line
        draw_transformed_line(50, 50, 100, 100, 3, tx=number_tx, ty=number_ty)

        # Scaled line
        draw_transformed_line(50, 50, 100, 100, 3, color=RED, sx=sx, sy=sy)

        # Rotated line
        draw_transformed_line(50, 50, 100, 100, 3, color=RED, angle=angle)

        pygame.display.flip()

if __name__ == "__main__":
    main()

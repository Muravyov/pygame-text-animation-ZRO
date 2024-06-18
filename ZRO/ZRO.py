import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Window settings
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Interactive ZRO text with wave animation')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Coordinates of points for each letter (shifted by 60 steps to the right)
letters = {
    'Z': [(160, 200), (180, 200), (200, 200), (220, 200), (240, 200), 
          (240, 220), (220, 240), (200, 260), (180, 280), (160, 300), 
          (160, 320), (180, 320), (200, 320), (220, 320), (240, 320)],
    'R': [(360, 200), (360, 220), (360, 240), (360, 260), (360, 280), 
          (360, 300), (380, 200), (400, 200), (420, 200), (440, 220), 
          (440, 240), (420, 260), (400, 260), (380, 260), (400, 280), 
          (420, 300), (440, 320), (360, 320)],
    'O': [(560, 200), (580, 200), (600, 200), (620, 200), (640, 220), 
          (640, 240), (640, 260), (640, 280), (640, 300), (620, 320), 
          (600, 320), (580, 320), (560, 320), (540, 300), (540, 280), 
          (540, 260), (540, 240), (540, 220)],
}

# Point size
point_radius = 10

# Main game loop
running = True
start_time = pygame.time.get_ticks()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black color
    window.fill(black)

    # Get the cursor position
    mouse_pos = pygame.mouse.get_pos()

    # Current time in milliseconds
    current_time = pygame.time.get_ticks() - start_time

    # Draw points for each letter with cursor hover check
    for letter, points in letters.items():
        for i, point in enumerate(points):
            # Calculate distance from cursor to point
            distance = math.sqrt((point[0] - mouse_pos[0]) ** 2 + (point[1] - mouse_pos[1]) ** 2)
            if distance < 100:  # If cursor is within 100 pixels from the point
                wave_offset = math.sin(current_time * 0.005 + distance / 10) * 5  # Sinusoidal wave with time and distance dependency
                animated_point = (point[0], point[1] + wave_offset)
            else:
                animated_point = point

            # Change point color on hover
            if (animated_point[0] - point_radius <= mouse_pos[0] <= animated_point[0] + point_radius) and (animated_point[1] - point_radius <= mouse_pos[1] <= animated_point[1] + point_radius):
                color = red
            else:
                color = white
            pygame.draw.circle(window, color, animated_point, point_radius)

    # Update the display
    pygame.display.flip()

    # Limit the FPS
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import random

# Set up pygame
pygame.init()

# Set up the window
width = 500
height = 500
window = pygame.display.set_mode((width, height))

# Set up the colors
black = (0, 0, 0)
green = (0, 255, 0)

# Set up the snake
snake_pos = [(width/2, height/2)]
snake_dir = (1, 0)

# Set up the food
food_pos = (random.randint(0, width), random.randint(0, height))

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the snake position
    snake_pos.insert(0, (snake_pos[0][0] + snake_dir[0], snake_pos[0][1] + snake_dir[1]))

    # Check for collisions
    if (
        snake_pos[0][0] < 0
        or snake_pos[0][1] < 0
        or snake_pos[0][0] >= width
        or snake_pos[0][1] >= height
        or snake_pos[0] in snake_pos[1:]
    ):
        pygame.quit()
        quit()

    # Check if the snake ate the food
    if snake_pos[0] == food_pos:
        food_pos = (random.randint(0, width), random.randint(0, height))
    else:
        snake_pos.pop()

    # Draw the snake and food
    window.fill(black)
    pygame.draw.rect(window, green, (food_pos[0], food_pos[1], 10, 10))
    for pos in snake_pos:
        pygame.draw.rect(window, green, (pos[0], pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(10)

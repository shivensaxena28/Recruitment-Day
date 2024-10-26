# Example booth positions (can be random or part of maze generation logic)
import pygame
from main import screen
import random

booths = [(100, 100), (600, 150), (300, 400)]

# Function to draw booths
def draw_booths():
    for booth in booths:
        pygame.draw.rect(screen, (0, 0, 255), (*booth, 40, 40))  # Blue booth squares

# In the main loop, add this to draw the booths
draw_booths()


def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    # Create a stack for the cells
    stack = []
    
    # Define directions for moving in the maze (down, up, right, left)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Randomly select a starting point
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    maze[start_y][start_x] = ' '  # Mark the start cell as a path
    stack.append((start_x, start_y))

    while stack:
        x, y = stack[-1]
        
        # Find the neighboring cells
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                neighbors.append((nx, ny))
        
        if neighbors:
            # Choose a random neighbor
            nx, ny = random.choice(neighbors)
            # Remove the wall between the current cell and the chosen cell
            maze[(y + ny) // 2][(x + nx) // 2] = ' '
            maze[ny][nx] = ' '  # Mark the chosen cell as a path
            stack.append((nx, ny))  # Add it to the stack
        else:
            stack.pop()  # Backtrack

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))
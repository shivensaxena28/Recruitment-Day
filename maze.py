# Example booth positions (can be random or part of maze generation logic)
import pygame
from main import SCREEN_HEIGHT, SCREEN_WIDTH, screen
import random
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Maze settings
CELL_SIZE = 80  # Increased cell size for larger spacing
MAZE_WIDTH = SCREEN_WIDTH // CELL_SIZE + 2  # Extra cells for off-screen visibility
MAZE_HEIGHT = SCREEN_HEIGHT // CELL_SIZE + 2  # Extra cells for off-screen visibility

# Example booth positions (scaled for new cell size)
booths = [(2, 2), (10, 3), (5, 7)]  # Adjusted booth positions

# Function to draw booths
def draw_booths():
    for booth in booths:
        x, y = booth
        pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate the maze
def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    stack = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    maze[start_y][start_x] = ' '  
    stack.append((start_x, start_y))

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = ' '
            maze[ny][nx] = ' '
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# Function to draw the maze
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell == ' ' else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

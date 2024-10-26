import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
PLAYER_SPEED = 4
FLASHLIGHT_LENGTH = 150  # Length of flashlight beam
TILE_SIZE = 80  # Size of each cell in pixels
COLLECTIBLE_COLOR = (255, 215, 0)  # Gold color for collectibles

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Career Maze: Dream for the Internship")

# Load assets (player image)
player_img = pygame.Surface((40, 40))
player_img.fill((0, 255, 0))  # Green player square

# Maze generation function
def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    stack = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    maze[start_y][start_x] = ' '  # Mark the start cell as a path
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

def draw_maze(screen, maze, camera):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell == '#' else BLACK
            pygame.draw.rect(screen, color, (x * TILE_SIZE + camera.camera.x, y * TILE_SIZE + camera.camera.y, TILE_SIZE, TILE_SIZE))

def generate_collectibles(maze):
    collectibles = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == ' ' and random.random() < 0.1:  # 10% chance to place a collectible
                collectibles.append((x, y))
    return collectibles

def draw_collectibles(screen, collectibles, camera):
    for (x, y) in collectibles:
        pygame.draw.rect(screen, COLLECTIBLE_COLOR, (x * TILE_SIZE + camera.camera.x, y * TILE_SIZE + camera.camera.y, TILE_SIZE // 2, TILE_SIZE // 2))

# Character class
class Character:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect(center=(x, y))
        self.maze_pos = (x // TILE_SIZE, y // TILE_SIZE)  # Track maze position

    def update(self, keys, maze):
        new_x, new_y = self.rect.x, self.rect.y
        
        if keys[pygame.K_LEFT]:
            new_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            new_x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            new_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            new_y += PLAYER_SPEED

        # Check for collisions with walls
        if maze[new_y // TILE_SIZE][new_x // TILE_SIZE] == ' ':
            self.rect.x, self.rect.y = new_x, new_y  # Move only if there's no wall

    def draw(self, screen, camera):
        screen.blit(self.image, self.rect.move(-camera.camera.x, -camera.camera.y))

# Camera class
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)
        x = min(0, x)
        x = max(-(self.width - self.camera.width), x)
        y = min(0, y)
        y = max(-(self.height - self.camera.height), y)
        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)

# Function to draw flashlight cone
def draw_flashlight(x, y, angle):
    end_x = x + FLASHLIGHT_LENGTH * math.cos(angle)
    end_y = y + FLASHLIGHT_LENGTH * math.sin(angle)
    pygame.draw.line(screen, WHITE, (x, y), (end_x, end_y), 2)

def main():
    # Maze dimensions
    maze_width, maze_height = 81, 81  # Larger maze
    maze = generate_maze(maze_width, maze_height)
    collectibles = generate_collectibles(maze)

    camera = Camera(maze_width * TILE_SIZE, maze_height * TILE_SIZE)  # Adjust for tile size
    player = Character(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # Start position of the player

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)  # Limit FPS to 60
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys pressed
        keys = pygame.key.get_pressed()

        # Player movement
        player.update(keys, maze)
        camera.update(player)  # Update camera based on player position

        # Draw the maze
        draw_maze(screen, maze, camera)

        # Draw collectibles
        draw_collectibles(screen, collectibles, camera)

        # Draw player
        player.draw(screen, camera)

        # Draw flashlight (basic direction right for now)
        flashlight_angle = 0  # Adjust this angle based on player direction (for now, it’s fixed)
        draw_flashlight(player.rect.centerx + camera.camera.x, player.rect.centery + camera.camera.y, flashlight_angle)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

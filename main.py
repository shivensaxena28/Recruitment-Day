import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (211, 211, 211)
PLAYER_SPEED = 4
FLASHLIGHT_CONE_ANGLE = math.radians(60)  # 60-degree flashlight cone
FLASHLIGHT_LENGTH = 150  # Length of flashlight beam

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Career Maze: Dream for the Internship")

# Load assets (player image)
player_img = pygame.Surface((10, 10))
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

def draw_maze(screen, maze):
    tile_size = 20  # Size of each cell in pixels
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = WHITE if cell == '#' else BLACK
            pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))

# Character class
class Character:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

def draw_fog(x, y):
    # Calculate the size of the fog rectangles
    fog_width = SCREEN_WIDTH
    fog_height = SCREEN_HEIGHT

    # Draw rectangles to cover the entire screen
    pygame.draw.rect(screen, RED, (0, 0, fog_width, y - 10))  # Top
    pygame.draw.rect(screen, RED, (0, y + 10, fog_width, fog_height - (y + 10)))  # Bottom
    pygame.draw.rect(screen, RED, (0, 0, x - 10, fog_height))  # Left
    pygame.draw.rect(screen, RED, (x + 10, 0, fog_width - (x + 10), fog_height))  # Right



def main():
    # Maze dimensions
    maze_width, maze_height = 41, 41  # Must be odd numbers
    maze = generate_maze(maze_width, maze_height)

    camera = Camera(maze_width * 20, maze_height * 20)  # Adjust for tile size
    player = Character(1 * 20, 1 * 20)  # Start position of the player

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
        player.update(keys)
        camera.update(player)  # Update camera based on player

        # Draw the maze
        draw_maze(screen, maze)

        draw_fog(player.rect.centerx, player.rect.centery)

        # Draw player at the camera-adjusted position
        screen.blit(player.image, camera.apply(player))

        # Draw flashlight (basic direction right for now)
        flashlight_angle = 0  # Adjust this angle based on player direction (for now, it’s fixed)
        #draw_flashlight(player.rect.centerx, player.rect.centery, flashlight_angle)

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
PLAYER_SPEED = 4
FLASHLIGHT_CONE_ANGLE = math.radians(60)  # 60-degree flashlight cone
FLASHLIGHT_LENGTH = 150  # Length of flashlight beam

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Recruitment Day")

# Load assets (placeholders for now)
player_img = pygame.Surface((40, 40))
player_img.fill((0, 255, 0))  # Green player square

# Game variables
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
clock = pygame.time.Clock()

# Function to draw the player
def draw_player(x, y):
    screen.blit(player_img, (x, y))

# Function to handle player movement
def handle_player_movement(keys_pressed, x, y):
    if keys_pressed[pygame.K_LEFT]:
        x -= PLAYER_SPEED
    if keys_pressed[pygame.K_RIGHT]:
        x += PLAYER_SPEED
    if keys_pressed[pygame.K_UP]:
        y -= PLAYER_SPEED
    if keys_pressed[pygame.K_DOWN]:
        y += PLAYER_SPEED
    return x, y

# Function to draw flashlight cone
def draw_flashlight(x, y, angle):
    end_x = x + FLASHLIGHT_LENGTH * math.cos(angle)
    end_y = y + FLASHLIGHT_LENGTH * math.sin(angle)
    pygame.draw.line(screen, WHITE, (x, y), (end_x, end_y), 2)

# Main loop
running = True
while running:
    clock.tick(60)  # Limit FPS to 60
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys_pressed = pygame.key.get_pressed()

    # Player movement
    player_x, player_y = handle_player_movement(keys_pressed, player_x, player_y)

    # Draw player
    draw_player(player_x, player_y)

    # Draw flashlight (basic direction right for now)
    flashlight_angle = 0  # Adjust this angle based on player direction (for now, it’s fixed)
    draw_flashlight(player_x + 20, player_y + 20, flashlight_angle)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()

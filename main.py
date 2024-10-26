import pygame


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

from maze import generate_maze, print_maze
from enemies import Enemy
from booths import draw_booths
from ui import title_screen, end_game_screen
from camera import Camera



# Assume Character is your player class with a rect attribute for positioning
class Character:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Career Maze: Dream for the Internship")

    camera = Camera(1600, 1600)  # Assuming the maze size is 1600x1600
    player = Character(400, 400)  # Start position of the player

    title_screen(screen)  # Show title screen

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        camera.update(player)  # Update the camera position based on player

        # Drawing the game elements
        screen.fill((0, 0, 0))  # Clear screen
        
        # Draw maze, enemies, and booths based on camera
        # Example: draw_maze(screen, camera)  # Implement this function in your maze logic
        generate_maze(player.x, player.y)

        # Draw player at the camera-adjusted position
        screen.blit(player.image, camera.apply(player))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

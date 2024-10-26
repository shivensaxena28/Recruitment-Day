import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Move entity's position based on camera's position
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Center the camera on the target (character)
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Keep the camera within the bounds of the maze
        x = min(0, x)  # Prevent the camera from going left
        x = max(-(self.width - self.camera.width), x)  # Prevent the camera from going right
        y = min(0, y)  # Prevent the camera from going up
        y = max(-(self.height - self.camera.height), y)  # Prevent the camera from going down

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)

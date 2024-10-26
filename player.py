class Player(pygame.sprite.Sprite):

        def __init__(self):

            super().__init__()

            self.image = pygame.image.load("player_sprite.png")  # Load your player image

            self.rect = self.image.get_rect()

            self.rect.x = screen_width // 2

            self.rect.y = screen_height // 2

            self.speed = 5  # Adjust speed as needed

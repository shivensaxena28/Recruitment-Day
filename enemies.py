import pygame
import random
import math
import main
from main import screen
from main import BLACK
from main import WHITE
from main import FLASHLIGHT_LENGTH
from main import player_x
from main import player_y
from main import flashlight_angle



class Enemy:
    def __init__(self, x, y, name, color, speed=2):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.stunned = False
        self.stun_timer = 0
        self.name = name

    def move(self):
        if not self.stunned:
            self.x += random.choice([-self.speed, 0, self.speed])
            self.y += random.choice([-self.speed, 0, self.speed])

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 40, 40))
        if self.stunned:
            text = pygame.font.Font(None, 24).render(self.name + " Stunned!", True, WHITE)
            screen.blit(text, (self.x, self.y - 20))

    def update_stun(self):
        if self.stunned:
            self.stun_timer -= 1
            if self.stun_timer <= 0:
                self.stunned = False

# Create enemies (peer, recruiter, professor)
enemies = [
    Enemy(200, 150, "Peer", (255, 0, 0)),
    Enemy(400, 300, "Recruiter", (255, 255, 0)),
    Enemy(100, 450, "Professor", (0, 255, 255))
]

# In the main loop, update and draw enemies
for enemy in enemies:
    enemy.move()
    enemy.draw()
    enemy.update_stun()


def check_flashlight_hit(enemy, player_x, player_y, flashlight_angle):
    # Simplified distance check for now
    dist = math.sqrt((enemy.x - player_x) ** 2 + (enemy.y - player_y) ** 2)
    if dist < FLASHLIGHT_LENGTH:  # Check if enemy is within flashlight distance
        # You could also check the angle for more precision
        return True
    return False

# In the main loop, stun enemies if the flashlight hits them
for enemy in enemies:
    if check_flashlight_hit(enemy, player_x, player_y, flashlight_angle):
        enemy.stunned = True
        enemy.stun_timer = 120  # Stun for 2 seconds (120 frames at 60 FPS)
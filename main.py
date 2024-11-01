import pygame
import math
from pygame.locals import *
from pygame import mixer

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, GRAY, YELLOW = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (169, 169, 169), (255,255,0)
PLAYER_SPEED = 1.75

FLAG_ONE_POSITION = (95, 520)
FLAG_ONE_RADIUS = 15

FLAG_TWO_POSITION = (635, 132)
FLAG_TWO_RADIUS = 15

FLAG_THREE_POSITION = (440, 310)
FLAG_THREE_RADIUS = 15

GOAL_POSITION = (770, 570)
GOAL_RADIUS = 15

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Midnight Maze")
pygame.display.set_caption("The Midnight Maze")

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
title_font = pygame.font.SysFont('Angels Message Formal', 72, pygame.font.Font.bold)
start_time = 30000
font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)
start_time = 30000
# Load assets (player image)
player_img = pygame.image.load("assets/MainCharacter.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (25, 25))

flag_img = pygame.image.load("assets/flag2.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (25, 25))

goal_img = pygame.image.load("assets/goal.png").convert_alpha()
goal_img = pygame.transform.scale(goal_img, (25, 25))

# Define maze walls as rectangles (x, y, width, height)
walls = [
    # Outer walls
    pygame.Rect(0, 0, SCREEN_WIDTH, 10),       # Top wall
    pygame.Rect(0, 0, 10, SCREEN_HEIGHT),       # Left wall
    pygame.Rect(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10),  # Bottom wall
    pygame.Rect(SCREEN_WIDTH - 10, 0, 10, SCREEN_HEIGHT),   # Right wall

]

walls2 = [
    # Inner walls
    pygame.Rect(60, 10, 10, 100), # First Down
    pygame.Rect(60, 160, 10, 200),# Second Down
    pygame.Rect(60, 410, 10, 140),# Third down
    pygame.Rect(220, 460, 10, 130),
    pygame.Rect(130, 470, 90, 70),
    pygame.Rect(70, 540, 150, 10), # Bottomost left across
    pygame.Rect(60,50,200,10), # first across
    pygame.Rect(120, 100, 190, 10),# second across
    pygame.Rect(70, 160, 160, 10), # third across
    pygame.Rect(220, 110, 10, 50),
    pygame.Rect(290, 160, 190, 10),# middle across middle
    pygame.Rect(290 , 160 , 10, 300),
    pygame.Rect(350, 50, 200, 10), # Top right block top
    pygame.Rect(540,50, 10, 180), # First down of third col
    pygame.Rect(600,10, 10, 50),
    pygame.Rect(600,100, 10, 50),
    pygame.Rect(600,200, 10, 160),
    pygame.Rect(600,200, 130, 10), #Right most middle across second
    pygame.Rect(600,150, 70, 10),
    pygame.Rect(610,50, 110, 10), #Right most First across
    pygame.Rect(610,100, 110, 10), # Right most second across
    pygame.Rect(720,100, 10, 100), # Right most third down
    pygame.Rect(660,260, 10, 160), # right most down middle
    pygame.Rect(360, 420, 380, 10), #Right Most middle across
    pygame.Rect(220, 470, 80, 10),
    pygame.Rect(360, 480, 330, 10), #Right Most middle across
    pygame.Rect(280, 530, 410, 10),
    pygame.Rect(360, 290, 10, 140),
    pygame.Rect(410, 280, 10, 90),
    pygame.Rect(410, 360, 50, 10),
    pygame.Rect(680, 530, 10, 60),
    pygame.Rect(680, 480, 10, 50),
    pygame.Rect(460, 220, 10, 140),
    pygame.Rect(520, 280, 10, 80),
    pygame.Rect(520, 280, 80, 10),
    pygame.Rect(460, 360, 100, 10),
    pygame.Rect(740, 420, 10, 100),
    pygame.Rect(740, 520, 50, 10),
    pygame.Rect(420, 330, 140, 30),
    pygame.Rect(720,260, 10, 100),  #right most down middle
    pygame.Rect(730,260, 60, 10),
    pygame.Rect(350, 100, 10, 60), #Top right block bottom
    pygame.Rect(350, 100, 100, 10),
    pygame.Rect(120, 460, 180, 10),
    pygame.Rect(120, 460, 10, 90),
    pygame.Rect(230 , 220, 10, 200),#Third down of Second lane
    pygame.Rect(70, 410, 170, 10), # fourth across
    pygame.Rect(170, 170, 10, 200),
    pygame.Rect(300, 10, 10, 90), #First down of Second Down
    pygame.Rect(290, 220, 250, 10), #First down of Second Down
    pygame.Rect(110, 220, 10 , 200), # Second Down of Second Down
]

def display_timer(screen, font, remaining_time):
    seconds = max(0, remaining_time // 1000)
    timer_text = font.render(f"Time: {seconds}", True, RED)
    screen.blit(timer_text, (SCREEN_WIDTH - 120, 10))

def display_message(screen, message, color,x,y):
    message_text = title_font.render(message, True, color)
    screen.blit(message_text, ((SCREEN_WIDTH + x) // 2 - message_text.get_width() // 2,
                                (SCREEN_HEIGHT + y) // 2 - message_text.get_height() // 2))

def display_message2(screen, message, color,x,y):
    message_text = font.render(message, True, color)
    screen.blit(message_text, ((SCREEN_WIDTH + x) // 2 - message_text.get_width() // 2,
                                (SCREEN_HEIGHT + y) // 2 - message_text.get_height() // 2))

def check_goal_reached(player):
    # Check if player has reached the goal 
    dist = math.sqrt((player.rect.centerx - GOAL_POSITION[0]) ** 2 +
                    (player.rect.centery - GOAL_POSITION[1]) ** 2)
    return dist <= GOAL_RADIUS  # Return True if within radius

# Flag class to represent the flags
class Flag:
    def __init__(self, x, y):
        self.image = flag_img
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, bol):
        if not bol:
            self.draw(screen)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


def check_flag_reached(player, x1, y1):
        # Check if player has reached the flag
        dist = math.sqrt((player.rect.centerx - x1) ** 2 +
                        (player.rect.centery - y1) ** 2)
        return dist <= GOAL_RADIUS  # Return True if it has

# Character class
class Character:
    def __init__(self, x, y):
        self.image = player_img
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys):
        # Move player based on keys pressed
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.check_collision(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.check_collision(PLAYER_SPEED, 0)
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
            self.check_collision(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
            self.check_collision(0, PLAYER_SPEED)

    def check_collision(self, dx, dy):
        # Check for collision with walls
        new_rect = self.rect.move(dx, dy)
        for wall in walls:
            if new_rect.colliderect(wall):
                # If colliding, reset position to avoid moving into the wall
                if dx > 0:  # Moving right
                    new_rect.right = wall.left
                if dx < 0:  # Moving left
                    new_rect.left = wall.right
                if dy > 0:  # Moving down
                    new_rect.bottom = wall.top
                if dy < 0:  # Moving up
                    new_rect.top = wall.bottom
                    
        for wall in walls2:
            if new_rect.colliderect(wall):
                # If colliding, reset position to avoid moving into the wall
                if dx > 0:  # Moving right
                    new_rect.right = wall.left
                if dx < 0:  # Moving left
                    new_rect.left = wall.right
                if dy > 0:  # Moving down
                    new_rect.bottom = wall.top
                if dy < 0:  # Moving up
                    new_rect.top = wall.bottom
                    
        self.rect = new_rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def draw_fog(x, y):
    # Calculate the size of the fog rectangles
    fog_width = SCREEN_WIDTH
    fog_height = SCREEN_HEIGHT
    keys = pygame.key.get_pressed()
    up = 10
    bot = 10
    left = 10
    right = 10
    if keys[pygame.K_LEFT]:
        left = 50
        bot = 20
        up = 20
    if keys[pygame.K_RIGHT]:
        right = 50
        bot = 20
        up = 20
    if keys[pygame.K_UP]:
        up = 50
        left = 20
        right = 20
    if keys[pygame.K_DOWN]:
        bot = 50
        left = 20
        right = 20
    keys = pygame.key.get_pressed()
    up = 10
    bot = 10
    left = 10
    right = 10
    if keys[pygame.K_LEFT]:
        left = 50
        bot = 20
        up = 20
    if keys[pygame.K_RIGHT]:
        right = 50
        bot = 20
        up = 20
    if keys[pygame.K_UP]:
        up = 50
        left = 20
        right = 20
    if keys[pygame.K_DOWN]:
        bot = 50
        left = 20
        right = 20
    # Draw rectangles to cover the entire screen
    pygame.draw.rect(screen, BLACK, (0, 0, fog_width, y - up))  # Top
    pygame.draw.rect(screen, BLACK, (0, y + bot, fog_width, fog_height - (y + bot)))  # Bottom
    pygame.draw.rect(screen, BLACK, (0, 0, x - left, fog_height))  # Left
    pygame.draw.rect(screen, BLACK, (x + right, 0, fog_width - (x + right), fog_height))  # Right
    up = 10
    bot = 10
    left = 10
    right = 10

def title_screen():
    while True:
        screen.fill(BLACK)
        display_message(screen, "THE MIDNIGHT MAZE", YELLOW, 0,0)
        display_message2(screen, "Get as many flags and reach the end before time runs out", WHITE, 0,100)
        display_message2(screen, "Press Enter to Start", RED, -10,150)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter is pressed
                    return  # Exit the title screen'''

def end_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter is pressed
                    main()
                    return  # Exit the title screen'''

def main():
    title_screen()
    #MUSIC
    mixer.init()
    mixer.music.load('Music.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play()
    player = Character(30, 30)  # Starting position
    flag1 = Flag(FLAG_ONE_POSITION[0], FLAG_ONE_POSITION[1])
    flag2 = Flag(FLAG_TWO_POSITION[0], FLAG_TWO_POSITION[1])
    flag3 = Flag(FLAG_THREE_POSITION[0], FLAG_THREE_POSITION[1])
    clock = pygame.time.Clock()
    running = True
    game_over = False
    win = False
    points = 0
    taken1 = False
    taken2 = False
    taken3 = False
    #tile_image = pygame.image.load("assets/tile1.png").convert_alpha()
    #tile_image = pygame.transform.scale(tile_image, (10, 60))
    goal_image = goal_img
    start_ticks = pygame.time.get_ticks()

    while running:
        elapsed_time = pygame.time.get_ticks() - start_ticks
        remaining_time = start_time - elapsed_time
        screen.fill(YELLOW)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        # Get keys pressed
        keys = pygame.key.get_pressed()

        # Update player
        player.update(keys)

        # Update flags
        if check_flag_reached(player, FLAG_ONE_POSITION[0], FLAG_ONE_POSITION[1]) and not taken1:
            taken1 = True
            points += 1
        elif not taken1:
            flag1.update(taken1)
        if check_flag_reached(player, FLAG_TWO_POSITION[0], FLAG_TWO_POSITION[1]) and not taken2:
            taken2 = True
            points += 1
        elif not taken2:
            flag2.update(taken2)
        if check_flag_reached(player, FLAG_THREE_POSITION[0], FLAG_THREE_POSITION[1]) and not taken3:
            taken3 = True
            points += 1
        elif not taken3:
            flag3.update(taken3)
   
        
            
            
        for wall in walls2:
            #screen.blit(tile_image, wall)
            pygame.draw.rect(screen, GRAY, wall)
               
        draw_fog(player.rect.centerx , player.rect.centery)  
         
        for wall in walls:
            pygame.draw.rect(screen, WHITE, wall)

        # Draw the goal before flipping the display
        screen.blit(goal_image, (750, 550))
        #pygame.draw.circle(screen, GREEN, GOAL_POSITION, GOAL_RADIUS)

        # Draw player
        player.draw(screen)

        # Display timer
        display_timer(screen, font, remaining_time)

        # Check for win condition
        if check_goal_reached(player):
            win = True
            game_over = True
        
        # Check for time up
        if remaining_time <= 0:
            game_over = True

        # Display game over messages
        if game_over:
            if win:
                screen.fill(BLACK)
                display_message(screen, "You Win !", GREEN,0,0)
                display_message2(screen, "We declare you the MAZE MASTER", GREEN,0,80)
                display_message2(screen, "Points:   " + str(points) + "/3", GREEN,0, 150)
                pygame.display.flip()  # Only flip once after all draw call
                running = False
            else:
                screen.fill(BLACK)
                display_message(screen, "You Lose", RED, 0,0)
                display_message2(screen, "Want to try again, press ENTER?", RED,0,100)
                display_message2(screen, "Points:   " + str(points) + "/3", RED,0,150)
                pygame.display.flip()  # Only flip once after all draw call
                end_screen()
                  # Wait for a moment before closing       
            pygame.display.flip()  # Only flip once after all draw calls
            pygame.time.delay(3000)  # Wait for a moment before closing
            running = False
        else:
            pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit FPS to 60
        
            
    pygame.quit()

if __name__ == "__main__":
    main()
# Example booth positions (can be random or part of maze generation logic)
booths = [(100, 100), (600, 150), (300, 400)]

# Function to draw booths
def draw_booths():
    for booth in booths:
        pygame.draw.rect(screen, (0, 0, 255), (*booth, 40, 40))  # Blue booth squares

# In the main loop, add this to draw the booths
draw_booths()

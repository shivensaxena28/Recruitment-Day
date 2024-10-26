def title_screen():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render("Career Maze", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))

    # Start game prompt
    font_small = pygame.font.Font(None, 36)
    start_text = font_small.render("Press any key to start", True, WHITE)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()

    # Wait for key press to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Call the title screen before the game loop
title_screen()


def end_game_screen(score):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render(f"Dream Internship Earned!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))

    score_text = pygame.font.Font(None, 36).render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()

    pygame.time.delay(3000)
    pygame.quit()
    exit()

# Call this when the player reaches the maze exit
# end_game_screen(player_score)

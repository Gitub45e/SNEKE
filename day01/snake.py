import pygame, random

import pick_up_sound.wav

# Initialize pygame
pygame.init()

# Set the display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

# Set colors
GREEN = (0, 255, 0)  # (r, g, b)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)
var = 518186

# Set fonts
font = pygame.font.SysFont('gabriola', 48)

# Set text
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: 0", True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKRED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sounds and music
pick_up_sound.wav  = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord: tuple[int, int, int, int] = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake_dx = -SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake_dx = 0
                snake_dy = -SNAKE_SIZE
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake_dx = 0
                snake_dy = SNAKE_SIZE

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snake body by one position in the list
body_coords =  head_coord

# Update the x,y position of the snake head and make a new coordinate
head_x += snake_dx
head_y += snake_dy
head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

# Check for game over
if head_x >= WINDOW_WIDTH or head_x < 0 or head_y >= WINDOW_HEIGHT or head_y < 0:
    running = False    # Update HUD
    pygame.mixer.Sound.play(pick_up_sound.wav)
    game_over_text = font.render("GAMEOVER", True, RED, DARKRED)
    game_over_rect = game_over_text.get_rect()

    display_surface.fill(DARKGREEN)


    display_surface.blit(score_text, score_rect)

    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)


    pygame.display.update()
    clock.tick(20)  


# Stop the game.
pygame.quit()

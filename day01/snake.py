import pygame
import random
import os

# --- 1. Initialize Pygame and Setup Window ---
pygame.init()

# Set the display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 12  # Lowered FPS slightly for smoother movement on a grid
clock = pygame.time.Clock()

# --- 2. Game Constants and Variables ---
SNAKE_SIZE = 20

# Colors
GREEN = (0, 200, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont('Gabriela', 48)

# Game State Variables
score = 0
snake_dx = SNAKE_SIZE  # Initial movement right
snake_dy = 0
game_status = 'PLAYING'  # 'PLAYING' or 'GAME_OVER'

# Sound setup (Requires 'pick_up_sound.wav' in the same directory)
try:
    pygame.mixer.init()
    pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")
except pygame.error:
    print("Warning: Sound file 'pick_up_sound.wav' not found. Sound disabled.")
if not pygame.mixer: print("Warning: ...")

# Create a placeholder object
class DummySound:
    def play(self):
        pass

pick_up_sound = DummySound()


# Create a placeholder object if sound fails to prevent crashes
def play(DummySound):

   pick_up_sound = DummySound()
# Initialize Snake Body and Apple
body_coords = []  # List of (x, y) tuples for each segment
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2


def random_apple_coord():
    """Generates a random coordinate for the apple on the grid."""
    # Ensure the apple is placed on a grid point
    rand_x = random.randint(0, (WINDOW_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    rand_y = random.randint(0, (WINDOW_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    return rand_x, rand_y, SNAKE_SIZE, SNAKE_SIZE


apple_coord = new_apple_coord = random_apple_coord()
apple_rect = pygame.Rect(apple_coord)

# --- 3. Game Functions ---

def reset_game():
    """Resets all game variables for a new game."""
    global score, head_x, head_y, snake_dx, snake_dy, body_coords, game_status, apple_coord, apple_rect
    score = 0
    head_x = WINDOW_WIDTH // 2
    head_y = WINDOW_HEIGHT // 2
    snake_dx = SNAKE_SIZE
    snake_dy = 0
    body_coords = []
    game_status = 'PLAYING'
    apple_coord = random_apple_coord()
    apple_rect = pygame.Rect(apple_coord)


def check_collisions():
    """Checks for boundary, self, and apple collisions."""
    global head_x, head_y, game_status, apple_coord, score

    head_rect = pygame.Rect(head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # 1. Check Boundary Collision
    if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
        game_status = 'GAME_OVER'
        return

    # 2. Check Self-Collision
    # Check if the head coordinates are in the body list (excluding the current head position)
    if (head_x, head_y) in [(x, y) for x, y, w, h in body_coords[1:]]:
        game_status = 'GAME_OVER'
        return

    # 3. Check Apple Collision
    if head_rect.colliderect(apple_rect):
        score += 1
import pick_up_sound.wav
play (pick_up_sound.wav)
 # Generate new apple coordinates
new_apple_coord = random_apple_coord()

#    Ensure the new apple does not spawn on the snake's body
    while new_apple_coord[0:2] in [(x, y) for x, y, w, h in body_coords]:
            new_apple_coord = random_apple_coord


        apple_coord = new_apple_coord
        # We DON'T pop the tail segment, allowing the snake to grow

    # If no apple collision, the snake moves, so the body needs to be trimmed
    else:
        # If the snake is not a single block, remove the tail
        if body_coords:
            body_coords.pop()


def draw_elements():
    """Draws all game elements to the display surface."""
    display_surface.fill(DARKGREEN)

    # Draw Apple
    pygame.draw.rect(display_surface, RED, apple_rect)

    # Draw Snake
    for segment in body_coords:
        pygame.draw.rect(display_surface, GREEN, segment)

    # Draw Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    display_surface.blit(score_text, (10, 10))


def draw_game_over():
    """Draws the Game Over screen."""
    display_surface.fill(DARKGREEN)

    game_over_text = font.render("GAME OVER", True, RED)
    game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 32))

    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 16))

    continue_text = font.render("Press SPACE to play again", True, WHITE)
    continue_rect = continue_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80))

    display_surface.blit(game_over_text, game_over_rect)
    display_surface.blit(final_score_text, final_score_rect)
    display_surface.blit(continue_text, continue_rect)


# --- 4. Main Game Loop ---
running = True
while running:
    # 4.1 Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_status == 'PLAYING':
                # Prevent immediate 180-degree turns
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake_dx == 0:
                    snake_dx = -SNAKE_SIZE
                    snake_dy = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake_dx == 0:
                    snake_dx = SNAKE_SIZE
                    snake_dy = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = -SNAKE_SIZE
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake_dy == 0:
                    snake_dx = 0
                    snake_dy = SNAKE_SIZE

            elif game_status == 'GAME_OVER':
                if event.key == pygame.K_SPACE:
                    reset_game()

    # 4.2 Game Logic Update (Only if playing)
    if game_status == 'PLAYING':
        # 1. Update Head Position
        head_x += snake_dx
        head_y += snake_dy

        # 2. Add the new head segment to the body list
        head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        body_coords.insert(0, head_coord)  # Prepend new head

        # 3. Check Collisions (This handles growth and setting GAME_OVER status)
        check_collisions()

    # 4.3 Drawing
    if game_status == 'PLAYING':
        draw_elements()
    elif game_status == 'GAME_OVER':
        draw_game_over()

    # 4.4 Update Display and Tick Clock
    pygame.display.update()
    clock.tick(FPS)

# --- 5. Clean Exit ---
pygame.quit()
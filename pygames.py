import pygame

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Movement Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = 375
player_y = 275
player_speed = 5

# Main game loop
running = True
while running:
    # Fill the screen with white
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update player position based on key press
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Draw the player (a red square)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()

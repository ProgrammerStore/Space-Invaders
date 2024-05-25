import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = (width - player_width) // 2
player_y = height - player_height - 10
player_speed = 5

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, width - enemy_width)
enemy_y = 0
enemy_speed = 3

# Bullet settings
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = height
bullet_speed = 10
bullet_fired = False

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bullet_fired:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullet_fired = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update enemy and bullet positions
    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = 0

    if bullet_fired:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_fired = False

    # Collision detection
    if enemy_y + enemy_height > bullet_y > enemy_y and enemy_x < bullet_x < enemy_x + enemy_width:
        enemy_x = random.randint(0, width - enemy_width)
        enemy_y = 0
        bullet_fired = False
        score += 1

    if enemy_y + enemy_height > player_y:
        pygame.quit()
        exit()

    # Clear the screen
    screen.fill(black)

    # Draw player, enemy, and bullet
    pygame.draw.rect(screen, green, pygame.Rect(player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, red, pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
    if bullet_fired:
        pygame.draw.rect(screen, white, pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the Pygame environment
pygame.quit()

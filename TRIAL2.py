import pygame
import webbrowser
from random import randint
from random import randrange
from sys import exit
import pyttsx3
import speech_recognition as sr

# Initialize Pygame and other modules
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('SUBG')
clock = pygame.time.Clock()

# Load assets (only showing some for brevity)
player_surf = pygame.image.load('OP/shinchan.png').convert_alpha()
player_jump = pygame.image.load('OP/jump.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 400))
background = pygame.image.load('OP/backb.png').convert_alpha()
background = pygame.transform.scale(background, (150, 100))
background_rect = background.get_rect(center=(925, 450))

text_font=pygame.font.Font(None, 45)


# Set initial values
player_gravity = 0
player_speed = 5

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = text_font.render('SCORE :' + str(current_time // 500), False, '#1CC809')
    score_rect = score_surf.get_rect(center=(75, 25))
    screen.blit(score_surf, score_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 410:
                player_gravity = -20  # Start jump
                player_surf = player_jump


    # Apply gravity
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 410:
        player_rect.bottom = 410
        player_surf = pygame.image.load('OP/shinchan.png').convert_alpha()  # Reset to running sprite

    # Get the current state of all keyboard keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Ensure the player stays within screen bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 1000:
        player_rect.right = 1000

    # Drawing everything on the screen
    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(background, background_rect)
    screen.blit(player_surf, player_rect)
    display_score()

    # Update the display
    pygame.display.update()
    clock.tick(60)

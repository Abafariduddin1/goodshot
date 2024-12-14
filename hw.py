import pygame
import random
import sys

pygame.init()


screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Good Shot Alien Game")

alien = pygame.image.load("L.5/ailein.png")
alien_rect = alien.get_rect(center=(100, 200))

score = 0
font = pygame.font.Font(None, 40)
message = "Shoot it!"
background_color = "white"

def move_alien():
    alien_rect.x = random.randint(0, 400 - alien_rect.width)
    alien_rect.y = random.randint(0, 600 - alien_rect.height)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if alien_rect.collidepoint(event.pos):
                score += 1
                message = "Nice shot!"
                move_alien()
                if score == 15:
                    background_color = "blue"
                    message = "Congrats on 15 points!"
            else:
                message = "You missed!"

    screen.fill(background_color)
    screen.blit(alien, alien_rect)
    score_text = font.render(f"Score: {score}", True, "black")
    message_text = font.render(message, True, "black")
    screen.blit(score_text, (10, 10))
    screen.blit(message_text, (100, 50))

    pygame.display.flip()
    clock.tick(60) 

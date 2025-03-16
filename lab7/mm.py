import pygame
import sys
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab7/clock.png")
background = pygame.transform.scale(background, (600, 600))
minute_hand = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab7/min.png")
second_hand = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab7/sec.png")

background_rect = background.get_rect(center=(300, 300))
minute_hand_rect = minute_hand.get_rect(center=(300, 300))
second_hand_rect = second_hand.get_rect(center=(300, 300))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes  # 360 degrees / 60 minutes
    second_angle = -6 * seconds  # 360 degrees / 60 seconds


    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_minute_hand_rect = rotated_minute_hand.get_rect(center=(300, 300))

    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle)
    rotated_second_hand_rect = rotated_second_hand.get_rect(center=(300, 300))


    screen.blit(background, background_rect)
    screen.blit(rotated_minute_hand, rotated_minute_hand_rect)
    screen.blit(rotated_second_hand, rotated_second_hand_rect)

    pygame.display.flip()

    clock.tick(60)

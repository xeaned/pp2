import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()

# Game constants
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
ENEMY_SPEED = 5  # Initial enemy speed

# Colors
LIGHT_PINK = (255, 182, 193)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font setup
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image and music
background = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/AnimatedStreet.png")
pygame.mixer.music.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/background.wav")
pygame.mixer.music.play(-1)

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Clock for FPS control
FramePerSec = pygame.time.Clock()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE, ENEMY_SPEED  # Accessing the global variables
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        # Increase enemy speed after every 10 coins collected
        if COINS >= (SCORE // 10) * 10:  # Every 10 coins collected
            ENEMY_SPEED = 5 + (COINS // 10)  # Increase the enemy speed

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/player.png")
        self.image = pygame.transform.scale(self.image, (50, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_type):
        super().__init__()
        self.coin_type = coin_type
        path = f"/Users/rapiyatleukhan/Desktop/pp2/lab9/race/{coin_type}.png"
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, 300))

        # Set coin value
        if coin_type == 'gold':
            self.value = 3
        elif coin_type == 'silver':
            self.value = 2
        else:
            self.value = 1

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
            new_coin = create_random_coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)

# Create a random coin with different probabilities
def create_random_coin():
    coin_choice = random.randint(1, 10)
    if coin_choice <= 2:
        return Coin('gold')
    elif coin_choice <= 6:
        return Coin('silver')
    else:
        return Coin('bronze')

# Create player, enemy, and initial coin
P1 = Player()
E1 = Enemy()
C1 = create_random_coin()

# Sprite groups
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)

# Speed increment event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED and SCORE >= 10:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Display score and coins
    DISPLAYSURF.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    DISPLAYSURF.blit(font_small.render(f"Coins: {COINS}", True, BLACK), (SCREEN_WIDTH - 120, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Handle coin collection
    collided_coin = pygame.sprite.spritecollideany(P1, coins)
    if collided_coin:
        COINS += collided_coin.value
        collided_coin.kill()
        new_coin = create_random_coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Handle enemy collision
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(LIGHT_PINK)
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(font_small.render(f"Score: {SCORE}", True, BLACK), (30, 320))
        DISPLAYSURF.blit(font_small.render(f"Coins Collected: {COINS}", True, BLACK), (30, 350))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

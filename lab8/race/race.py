import pygame, sys
from pygame.locals import *
import random, time

# Initialize the pygame library
pygame.init()

# Setting up frames per second (FPS)
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
LIGHT_PINK = (255, 182, 193)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game variables
SCREEN_WIDTH = 400  # Width of the game screen
SCREEN_HEIGHT = 600  # Height of the game screen
SPEED = 5  # Initial speed of enemies
SCORE = 0  # Player's score
COINS = 0  # Coins collected by the player

# Setting up fonts for text display
font = pygame.font.SysFont("Verdana", 60)  # Large font for "Game Over"
font_small = pygame.font.SysFont("Verdana", 20)  # Smaller font for scores
game_over = font.render("Game Over", True, BLACK)  # Rendered "Game Over" text

# Loading background image
background = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/AnimatedStreet.png")

# Loading and playing background music
pygame.mixer.music.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/background.wav")
pygame.mixer.music.play(-1)  # Loop the background music indefinitely

# Setting up the game display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)  # Fill the screen with white color initially
pygame.display.set_caption("Game")  # Set the window title

# Enemy class for handling enemy behavior
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 120))  # Resize the enemy sprite
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Random starting position

    def move(self):
        # Move the enemy downward and reset if it moves off-screen
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1  # Increase score when the enemy moves out
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class for handling player behavior
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/player.png")
        self.image = pygame.transform.scale(self.image, (50, 120))  # Resize the player sprite
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Initial position

    def move(self):
        # Move the player left or right based on key presses
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:  # Check boundary on the left
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # Check boundary on the right
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Coin class for handling collectible coin behavior
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab8/race/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the coin sprite
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, 300))  # Random position

    def move(self):
        # Move the coin downward and reset position when it moves off-screen
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, 300))

# Creating instances of Player, Enemy, and Coin
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Grouping sprites for collision detection and updates
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a custom event to increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Trigger every 1 second

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:  # Increment speed periodically
            SPEED += 0.5
        if event.type == QUIT:  # Exit the game
            pygame.quit()
            sys.exit()

    # Draw the background
    DISPLAYSURF.blit(background, (0, 0))
    
    # Display the score and coins collected
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_collected = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected, (SCREEN_WIDTH - 120, 10))

    # Update and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision between player and coins
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1  # Increment coin count
        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, 300))

    # Check for collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/rapiyatleukhan/Desktop/pp2/lab8/race/crash.wav').play()
        time.sleep(1)
        
        # Display game over screen
        DISPLAYSURF.fill(LIGHT_PINK)
        DISPLAYSURF.blit(game_over, (30, 250))
        final_score = font_small.render(f"Score: {SCORE}", True, BLACK)
        final_coins = font_small.render(f"Coins Collected: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_score, (30, 320))
        DISPLAYSURF.blit(final_coins, (30, 350))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Remove all sprites
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

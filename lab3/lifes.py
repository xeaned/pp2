import pygame
import random
import time
import os

# Initialize Pygame
pygame.init()

# Set up screen dimensions and cell size
WIDTH = 600
HEIGHT = 600
CELL = 30

# Create display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set font for score, level, and lives display
font = pygame.font.SysFont("Arial", 24)

# Draw a checkerboard grid for the game background
def draw_grid():
    colors = [(144, 238, 144), (60, 179, 113)]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Class to represent a point (used for snake body and food)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Snake class definition
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # Initial body segments
        self.dx = 1  # Horizontal movement
        self.dy = 0  # Vertical movement

    # Move the snake by updating the position of each segment
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    # Draw the snake segments and eyes
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, (70, 130, 180), (head.x * CELL, head.y * CELL, CELL, CELL))
        eye_size = CELL // 8
        eye_offset = CELL // 4
        pygame.draw.circle(screen, (0, 0, 0), (head.x * CELL + eye_offset, head.y * CELL + eye_offset), eye_size)
        pygame.draw.circle(screen, (0, 0, 0), (head.x * CELL + CELL - eye_offset, head.y * CELL + eye_offset), eye_size)
        for segment in self.body[1:]:
            pygame.draw.rect(screen, (70, 130, 180), (segment.x * CELL, segment.y * CELL, CELL, CELL))

    # Check if the snake's head collides with its body
    def check_collision_with_self(self):
        head = self.body[0]
        return any(head.x == s.x and head.y == s.y for s in self.body[1:])

    # Check if the snake collides with walls
    def check_collision_with_walls(self):
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    # Check if the snake eats food
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))  # Extend body based on fruit weight
            food.generate_random_pos(self)
            return food.weight
        return 0

# Food class definition
class Food:
    def __init__(self):
        # Load images for different food types
        self.images = {
            "strawberry": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/strawberry.png"),
            "cherry": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/cherry.png"),
            "watermelon": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/watermelon.png"),
        }
        self.image = None
        self.pos = Point(5, 5)
        self.weight = 1
        self.generate_random_type()
        self.creation_time = time.time()
        self.time_limit = 5  # seconds before food disappears

    # Choose a random fruit type and set its weight and image
    def generate_random_type(self):
        fruit_type = random.choice(["strawberry", "cherry", "watermelon"])
        self.image = pygame.transform.scale(self.images[fruit_type], (CELL, CELL))
        self.weight = {"strawberry": 1, "cherry": 2, "watermelon": 3}[fruit_type]

    # Draw the food on screen
    def draw(self):
        screen.blit(self.image, (self.pos.x * CELL, self.pos.y * CELL))

    # Generate a new random position for the food that doesn't overlap with the snake
    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if all(segment.x != x or segment.y != y for segment in snake.body):
                self.pos = Point(x, y)
                self.generate_random_type()
                self.creation_time = time.time()
                break

    # Check if the food should disappear after a time limit
    def check_expiration(self):
        return time.time() - self.creation_time > self.time_limit

# === Main Game Setup ===
FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = Food()
score = 0
level = 1
lives = 3  # Start with 3 lives

# === Main Game Loop ===
running = True
while running:
    # Event handling for quitting and key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Movement controls (no 180-degree turns)
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1

    # Clear screen and draw grid
    screen.fill((0, 0, 0))
    draw_grid()

    # Update snake position
    snake.move()

    # Check for self-collision
    if snake.check_collision_with_self():
        print("Game Over! Snake collided with itself.")
        running = False

    # Check for wall collision
    if snake.check_collision_with_walls():
        print("Wall Collision! Lost a life.")
        lives -= 1
        if lives > 0:
            # Reset snake position after wall collision
            snake = Snake()  # Reset snake to initial state
        else:
            print("Game Over! No lives left.")
            running = False

    # Check for food collision and update score/level
    gained = snake.check_collision(food)
    if gained:
        score += gained
        if score % 10 == 0:
            level += 1
            FPS += 1  # Increase speed with each level

    # If food expires, generate new one
    if food.check_expiration():
        food.generate_random_pos(snake)

    # Draw everything
    snake.draw()
    food.draw()

    # Show score, level, and lives
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (10, 40))
    screen.blit(font.render(f"Lives: {lives}", True, (255, 0, 0)), (WIDTH - 100, 10))

    # Refresh display and tick clock
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame when game ends
pygame.quit()

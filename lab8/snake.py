import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

CELL = 30

# Fonts for score and level display
font = pygame.font.SysFont("Arial", 24)

# Function to draw the grid with alternating colors
def draw_grid():
    colors = [(144, 238, 144), (60, 179, 113)]  # Light green and green
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Class representing a point in the grid
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

# Class representing the Snake
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # Initial body
        self.dx = 1  # Horizontal direction
        self.dy = 0  # Vertical direction

    def move(self):
        # Move the body segments
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Move the head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        # Draw the head with eyes
        head = self.body[0]
        pygame.draw.rect(screen, (70, 130, 180), (head.x * CELL, head.y * CELL, CELL, CELL))  # Blue color
        eye_size = CELL // 8
        eye_offset = CELL // 4
        pygame.draw.circle(screen, (0, 0, 0), (head.x * CELL + eye_offset, head.y * CELL + eye_offset), eye_size)  # Left eye
        pygame.draw.circle(screen, (0, 0, 0), (head.x * CELL + CELL - eye_offset, head.y * CELL + eye_offset), eye_size)  # Right eye
        # Draw the body
        for segment in self.body[1:]:
            pygame.draw.rect(screen, (70, 130, 180), (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_with_self(self):
        # Check if the head collides with any body segment
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def check_collision_with_walls(self):
        # Check if the head collides with the walls
        head = self.body[0]
        return head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL

    def check_collision(self, food):
        # Check if the snake eats the food
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))  # Grow the snake
            food.generate_random_pos(self)  # Generate new food position
            return True
        return False

# Class representing the Food
class Food:
    def __init__(self):
        self.pos = Point(9, 9)  # Initial position

    def draw(self):
        # Draw the food with a red color and black border
        pygame.draw.rect(screen, (178, 34, 34), (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))  # Red color
        pygame.draw.rect(screen, (0, 0, 0), (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 1)  # Black border

    def generate_random_pos(self, snake):
        # Generate a random position that does not overlap with the snake
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if all(segment.x != x or segment.y != y for segment in snake.body):
                self.pos = Point(x, y)
                break

# Initialize game variables
FPS = 5  # Frames per second
clock = pygame.time.Clock()

food = Food()
snake = Snake()
score = 0  # Player's score
level = 1  # Current level
food_to_next_level = 3  # Foods required to level up

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quit the game
        if event.type == pygame.KEYDOWN:
            # Handle snake direction changes
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

    screen.fill(colorBLACK)  # Clear the screen

    draw_grid()  # Draw the background grid

    snake.move()  # Move the snake

    # Check for collisions
    if snake.check_collision_with_self() or snake.check_collision_with_walls():
        print("Game Over!")
        running = False  # End the game

    if snake.check_collision(food):
        score += 1  # Increase score
        food_to_next_level -= 1  # Decrease foods required for the next level

        if food_to_next_level == 0:
            level += 1  # Increase level
            food_to_next_level = 3  # Reset foods required for the next level
            FPS += 1  # Increase game speed

    snake.draw()  # Draw the snake
    food.draw()  # Draw the food

    # Display score and level
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()  # Update the screen
    clock.tick(FPS)  # Control game speed

pygame.quit()

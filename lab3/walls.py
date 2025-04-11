import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up screen dimensions and cell size
WIDTH = 600
HEIGHT = 600
CELL = 30

# Colors
COLOR_OLIVE = (85, 107, 47)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (200, 200, 200)
COLOR_YELLOW = (255, 255, 0)
COLOR_SNAKE = (70, 130, 180)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_LIGHTBLUE = (173, 216, 230)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_PURPLE = (128, 0, 128)
COLOR_YELLOW = (255, 255, 0)
# Create display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set font for score and level display
font = pygame.font.SysFont("Arial", 24)

# Wall coordinates
coords_wall = [(9, 9), (10, 9), (9, 10), (10, 10)]

# Draw grid and wall blocks
def draw_board_with_walls():
    colors = [(144, 238, 144), (60, 179, 113)]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))
            if (i, j) in coords_wall:
                pygame.draw.rect(screen, COLOR_OLIVE, (i * CELL, j * CELL, CELL, CELL))

# Point class for snake and food
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Snake class
class Snake:
    def __init__(self):
        self.body = [Point(5, 5), Point(5, 6), Point(5, 7)]

        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, COLOR_SNAKE, (head.x * CELL, head.y * CELL, CELL, CELL))
        eye_size = CELL // 8
        eye_offset = CELL // 4
        pygame.draw.circle(screen, COLOR_BLACK, (head.x * CELL + eye_offset, head.y * CELL + eye_offset), eye_size)
        pygame.draw.circle(screen, COLOR_BLACK, (head.x * CELL + CELL - eye_offset, head.y * CELL + eye_offset), eye_size)
        for segment in self.body[1:]:
            pygame.draw.rect(screen, COLOR_SNAKE, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_with_self(self):
        head = self.body[0]
        return any(head.x == s.x and head.y == s.y for s in self.body[1:])

    def check_collision_with_walls(self):
        head = self.body[0]
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        for wx, wy in coords_wall:
            if head.x == wx and head.y == wy:
                return True
        return False

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self)
            return food.weight
        return 0

# Food class
class Food:
    def __init__(self):
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
        self.time_limit = 5

    def generate_random_type(self):
        fruit_type = random.choice(["strawberry", "cherry", "watermelon"])
        self.image = pygame.transform.scale(self.images[fruit_type], (CELL, CELL))
        self.weight = {"strawberry": 1, "cherry": 2, "watermelon": 3}[fruit_type]

    def draw(self):
        screen.blit(self.image, (self.pos.x * CELL, self.pos.y * CELL))

    def generate_random_pos(self, snake):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            occupied = any(segment.x == x and segment.y == y for segment in snake.body)
            on_wall = (x, y) in coords_wall
            if not occupied and not on_wall:
                self.pos = Point(x, y)
                self.generate_random_type()
                self.creation_time = time.time()
                break

    def check_expiration(self):
        return time.time() - self.creation_time > self.time_limit

# === Main Game Setup ===
FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = Food()
score = 0
level = 1

# === Main Game Loop ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
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

    screen.fill(COLOR_BLACK)
    draw_board_with_walls()
    snake.move()

    if snake.check_collision_with_self() or snake.check_collision_with_walls():
        print("Game Over!")
        running = False

    gained = snake.check_collision(food)
    if gained:
        score += gained
        if score % 10 == 0:
            level += 1
            FPS += 1

    if food.check_expiration():
        food.generate_random_pos(snake)

    snake.draw()
    food.draw()

    screen.blit(font.render(f"Score: {score}", True, COLOR_BLACK), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, COLOR_BLACK), (10, 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

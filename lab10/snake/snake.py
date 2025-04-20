import pygame
import random
import time
import psycopg2

# ========== DATABASE SETUP ==========
conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",       
    password="12345678" 
)
cur = conn.cursor()

# Создание таблиц
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1
);
""")
conn.commit()

# ========== USER LOGIN ==========
def get_or_create_user():
    while True:
        name = input("Enter your username or type 'printall' to see all scores: ").strip()
        if name.lower() == 'printall':
            cur.execute("""
                SELECT users.id, users.username, user_score.score, user_score.level
                FROM users
                JOIN user_score ON users.id = user_score.user_id
            """)
            rows = cur.fetchall()
            print("\n=== Users ===")
            for row in rows:
                print(f"ID: {row[0]}, Username: {row[1]}, Score: {row[2]}, Level: {row[3]}")
            print("=============\n")
        else:
            cur.execute("SELECT id FROM users WHERE username = %s", (name,))
            user = cur.fetchone()
            if not user:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (name,))
                user_id = cur.fetchone()[0]
                conn.commit()
                print(f"New user '{name}' created.")
            else:
                user_id = user[0]

            cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
            data = cur.fetchone()
            if not data:
                cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (user_id,))
                conn.commit()
                score, level = 0, 1
            else:
                score, level = data
            return user_id, name, score, level

user_id, username, score, level = get_or_create_user()

# ========== GAME SETUP ==========
pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Snake - {username}")
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
FPS = 5 + level - 1  # Speed grows with level

class Point:
    def __init__(self, x, y): self.x, self.y = x, y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        for i, segment in enumerate(self.body):
            color = (70, 130, 180) if i else (30, 144, 255)
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision_self(self):
        head = self.body[0]
        return any(head.x == s.x and head.y == s.y for s in self.body[1:])

    def check_collision_wall(self):
        head = self.body[0]
        return not (0 <= head.x < WIDTH // CELL and 0 <= head.y < HEIGHT // CELL)

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            for _ in range(food.weight):
                self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self)
            return food.weight
        return 0

class Food:
    def __init__(self):
        self.images = {
            "strawberry": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/strawberry.png"),
            "cherry": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/cherry.png"),
            "watermelon": pygame.image.load("/Users/rapiyatleukhan/Desktop/pp2/lab9/snake/watermelon.png")
        }
        self.image = None
        self.pos = Point(5, 5)
        self.weight = 1
        self.generate_random_type()
        self.creation_time = time.time()
        self.time_limit = 10

    def generate_random_type(self):
        fruit = random.choice(["strawberry", "cherry", "watermelon"])
        self.image = pygame.transform.scale(self.images[fruit], (CELL, CELL))
        self.weight = {"strawberry": 1, "cherry": 2, "watermelon": 3}[fruit]

    def generate_random_pos(self, snake):
        while True:
            x, y = random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)
            if all(s.x != x or s.y != y for s in snake.body):
                self.pos = Point(x, y)
                self.generate_random_type()
                self.creation_time = time.time()
                break

    def draw(self):
        screen.blit(self.image, (self.pos.x * CELL, self.pos.y * CELL))

    def expired(self):
        return time.time() - self.creation_time > self.time_limit

def draw_grid():
    colors = [(144, 238, 144), (60, 179, 113)]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (j * CELL, i * CELL, CELL, CELL))

snake = Snake()
food = Food()
running, paused = True, False

# ========== GAME LOOP ==========
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Paused")
                else:
                    print("Resumed")
            if not paused:
                if event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.dx, snake.dy = 1, 0
                elif event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.dx, snake.dy = -1, 0
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.dx, snake.dy = 0, 1
                elif event.key == pygame.K_UP and snake.dy == 0:
                    snake.dx, snake.dy = 0, -1

    if paused:
        continue

    snake.move()
    if snake.check_collision_self() or snake.check_collision_wall():
        print("Game Over!")
        break

    gained = snake.check_collision(food)
    if gained:
        score += gained
        if score % 10 == 0:
            level += 1
            FPS += 1

    if food.expired():
        food.generate_random_pos(snake)

    screen.fill((0, 0, 0))
    draw_grid()
    snake.draw()
    food.draw()
    screen.blit(font.render(f"User: {username}", True, (0, 0, 0)), (10, 5))
    screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 30))
    screen.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (10, 55))
    pygame.display.flip()
    clock.tick(FPS)

# ========== SAVE ON EXIT ==========
cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
conn.commit()
cur.close()
conn.close()
pygame.quit()

import pygame
import sys

pygame.init()

# Main parameters
WIDTH, HEIGHT = 1200, 800
FPS = 60
WHITE = (255, 255, 255)
DARK_GRAY = (60, 60, 60)
LIGHT_GRAY = (180, 180, 180)
BLACK = (0, 0, 0)

# Screen and font initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# Initial settings
color = BLACK
radius = 10
mode = "pen"
drawing = False
start_pos = None
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Colors and buttons
colors = {"Black": BLACK, "Red": (255, 0, 0), "Green": (0, 255, 0), "Blue": (0, 0, 255), "Yellow": (255, 255, 0)}
buttons = []

# Function to create a button
def create_button(rect, label, action):
    buttons.append({"rect": pygame.Rect(rect), "label": label, "action": action})

# Function to draw buttons
def draw_buttons():
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, 200, HEIGHT))  # Sidebar
    for btn in buttons:
        pygame.draw.rect(screen, LIGHT_GRAY, btn["rect"])
        text_color = BLACK
        if btn["action"] in colors:
            text_color = colors[btn["action"]]
        text = font.render(btn["label"], True, text_color)
        screen.blit(text, (btn["rect"].x + 10, btn["rect"].y + 10))

# Function to handle button clicks
def handle_button_click(pos):
    global mode, color, radius, canvas
    for btn in buttons:
        if btn["rect"].collidepoint(pos):
            action = btn["action"]
            if action == "clear":
                canvas.fill(WHITE)
            elif action == "increase":
                radius = min(radius + 2, 100)
            elif action == "decrease":
                radius = max(radius - 2, 1)
            elif action in colors:
                color = colors[action]
            else:
                mode = action

# Create tool buttons
create_button((10, 10, 180, 40), "Pen", "pen")
create_button((10, 60, 180, 40), "Eraser", "erase")
create_button((10, 110, 180, 40), "Draw rectangle", "rect")
create_button((10, 160, 180, 40), "Draw circle", "circle")
create_button((10, 210, 180, 40), "Clear", "clear")

# Create color buttons
y = 270
for label in colors:
    create_button((10, y, 180, 40), label, label)
    y += 50

# Create brush size buttons
create_button((10, y, 85, 40), "+", "increase")
create_button((105, y, 85, 40), "-", "decrease")

# Main loop
while True:
    screen.blit(canvas, (0, 0))  # Draw the canvas
    draw_buttons()              # Draw the buttons

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] <= 200:
                handle_button_click(event.pos)
            else:
                drawing = True
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                end_pos = event.pos
                if mode == "rect":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, radius)
                elif mode == "circle":
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius_circle = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(canvas, color, center, radius_circle, radius)
            drawing = False
            start_pos = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode in ["pen", "erase"]:
                end_pos = event.pos
                draw_color = color if mode == "pen" else WHITE
                if start_pos is not None:
                    pygame.draw.line(canvas, draw_color, start_pos, end_pos, radius * 2)
                    pygame.draw.circle(canvas, draw_color, start_pos, int(radius * 0.6))
                    pygame.draw.circle(canvas, draw_color, end_pos, int(radius * 0.6))
                start_pos = end_pos

    # Display brush size
    pygame.draw.rect(screen, DARK_GRAY, (WIDTH - 130, 10, 120, 40))
    size_display = font.render(f"Size: {radius}", True, WHITE)
    screen.blit(size_display, (WIDTH - 120, 15))

    pygame.display.flip()
    clock.tick(FPS)

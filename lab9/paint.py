import pygame
import sys
import math

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
            elif action == "pen":
                mode = action
            elif action == "erase":
                mode = action
            elif action == "rect":
                mode = action
            elif action == "circle":
                mode = action
            elif action == "square":
                mode = action
            elif action == "right_triangle":
                mode = action
            elif action == "equilateral_triangle":
                mode = action
            elif action == "rhombus":
                mode = action
            elif action in colors:
                color = colors[action]

# Function to draw a square
def draw_square(start, end, color, radius):
    side_length = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), side_length, side_length)
    pygame.draw.rect(screen, color, rect, radius)

# Function to draw a right triangle
def draw_right_triangle(start, end, color, radius):
    base_length = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    if end[0] > start[0] and end[1] > start[1]:
        points = [(start[0], start[1]), (start[0] + base_length, start[1]), (start[0], start[1] + height)]
    elif end[0] < start[0] and end[1] < start[1]:
        points = [(start[0], start[1]), (start[0] - base_length, start[1]), (start[0], start[1] - height)]
    elif end[0] < start[0] and end[1] > start[1]:
        points = [(start[0], start[1]), (start[0] - base_length, start[1]), (start[0], start[1] + height)]
    else:  # end[0] > start[0] and end[1] < start[1]
        points = [(start[0], start[1]), (start[0] + base_length, start[1]), (start[0], start[1] - height)]
    pygame.draw.polygon(screen, color, points, radius)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(start, end, color, radius):
    side_length = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    height = math.sqrt(3) * side_length / 2
    points = [
        (start[0], start[1] + height),
        (start[0] + side_length, start[1] + height),
        (start[0] + side_length / 2, start[1] - height)
    ]
    pygame.draw.polygon(screen, color, points, radius)

# Function to draw a rhombus
def draw_rhombus(start, end, color, radius):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    points = [
        (start[0] + width / 2, start[1]),
        (start[0] + width, start[1] + height / 2),
        (start[0] + width / 2, start[1] + height),
        (start[0], start[1] + height / 2)
    ]
    pygame.draw.polygon(screen, color, points, radius)

# Create tool buttons
create_button((10, 10, 180, 40), "Pen", "pen")
create_button((10, 60, 180, 40), "Eraser", "erase")
create_button((10, 110, 180, 40), "Draw rectangle", "rect")
create_button((10, 160, 180, 40), "Draw circle", "circle")
create_button((10, 210, 180, 40), "Draw square", "square")
create_button((10, 260, 180, 40), "Draw right triangle", "right_triangle")
create_button((10, 310, 180, 40), "Draw equilateral triangle", "equilateral_triangle")
create_button((10, 360, 180, 40), "Draw rhombus", "rhombus")
create_button((10, 410, 180, 40), "Clear", "clear")

# Create color buttons
y = 470
for label in colors:
    create_button((10, y, 180, 40), label, label)
    y += 50

# Create brush size buttons
create_button((10, y, 85, 40), "+", "increase")
create_button((105, y, 85, 40), "-", "decrease")

# Main loop
while True:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))  # Draw the canvas on the screen
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
                # Save the shape to the canvas when mouse is released
                if mode == "rect":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, radius)
                elif mode == "circle":
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    radius_circle = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(canvas, color, center, radius_circle, radius)
                elif mode == "square":
                    draw_square(start_pos, end_pos, color, radius)
                    # Save square to canvas
                    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), side_length, side_length)
                    pygame.draw.rect(canvas, color, rect, radius)
                elif mode == "right_triangle":
                    draw_right_triangle(start_pos, end_pos, color, radius)
                    # Save right triangle to canvas
                    base_length = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    if end_pos[0] > start_pos[0] and end_pos[1] > start_pos[1]:
                        points = [(start_pos[0], start_pos[1]), (start_pos[0] + base_length, start_pos[1]), (start_pos[0], start_pos[1] + height)]
                    elif end_pos[0] < start_pos[0] and end_pos[1] < start_pos[1]:
                        points = [(start_pos[0], start_pos[1]), (start_pos[0] - base_length, start_pos[1]), (start_pos[0], start_pos[1] - height)]
                    elif end_pos[0] < start_pos[0] and end_pos[1] > start_pos[1]:
                        points = [(start_pos[0], start_pos[1]), (start_pos[0] - base_length, start_pos[1]), (start_pos[0], start_pos[1] + height)]
                    else:  # end_pos[0] > start_pos[0] and end_pos[1] < start_pos[1]
                        points = [(start_pos[0], start_pos[1]), (start_pos[0] + base_length, start_pos[1]), (start_pos[0], start_pos[1] - height)]
                    pygame.draw.polygon(canvas, color, points, radius)
                elif mode == "equilateral_triangle":
                    draw_equilateral_triangle(start_pos, end_pos, color, radius)
                    # Save equilateral triangle to canvas
                    side_length = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    height = math.sqrt(3) * side_length / 2
                    points = [
                        (start_pos[0], start_pos[1] + height),
                        (start_pos[0] + side_length, start_pos[1] + height),
                        (start_pos[0] + side_length / 2, start_pos[1] - height)
                    ]
                    pygame.draw.polygon(canvas, color, points, radius)
                elif mode == "rhombus":
                    draw_rhombus(start_pos, end_pos, color, radius)
                    # Save rhombus to canvas
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    points = [
                        (start_pos[0] + width / 2, start_pos[1]),
                        (start_pos[0] + width, start_pos[1] + height / 2),
                        (start_pos[0] + width / 2, start_pos[1] + height),
                        (start_pos[0], start_pos[1] + height / 2)
                    ]
                    pygame.draw.polygon(canvas, color, points, radius)
            drawing = False
            start_pos = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode in ["pen", "erase"]:
                end_pos = event.pos
                draw_color = color if mode == "pen" else WHITE
                if start_pos is not None:
                    pygame.draw.line(canvas, draw_color, start_pos, end_pos, radius * 2)  # Draw on canvas
                    pygame.draw.circle(canvas, draw_color, start_pos, int(radius * 0.6))  # Draw on canvas
                    pygame.draw.circle(canvas, draw_color, end_pos, int(radius * 0.6))  # Draw on canvas
                start_pos = end_pos

            # Drawing preview for other shapes
            elif mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                   abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                screen.blit(canvas, (0, 0))  # Keep previous shapes on the screen
                pygame.draw.rect(screen, color, rect, radius)

            elif mode == "circle":
                end_pos = event.pos
                center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                radius_circle = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                screen.blit(canvas, (0, 0))  # Keep previous shapes on the screen
                pygame.draw.circle(screen, color, center, radius_circle, radius)

            elif mode == "square":
                end_pos = event.pos
                draw_square(start_pos, end_pos, color, radius)

            elif mode == "right_triangle":
                end_pos = event.pos
                draw_right_triangle(start_pos, end_pos, color, radius)

            elif mode == "equilateral_triangle":
                end_pos = event.pos
                draw_equilateral_triangle(start_pos, end_pos, color, radius)

            elif mode == "rhombus":
                end_pos = event.pos
                draw_rhombus(start_pos, end_pos, color, radius)

    # Display brush size

    brush_size_text = font.render(f"size {radius}", True, LIGHT_GRAY)
    screen.blit(brush_size_text, (14, 762))

    pygame.display.update()
    clock.tick(FPS)


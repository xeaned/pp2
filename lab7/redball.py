import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((800, 480))

COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

rect_x = (WIDTH - 50) // 2
rect_y = (HEIGHT - 50) // 2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and rect_y > 0:
        rect_y -= 20
    if pressed_keys[pygame.K_DOWN] and rect_y < (HEIGHT - 50):
        rect_y += 20
    if pressed_keys[pygame.K_RIGHT] and rect_x < (WIDTH - 50):
        rect_x += 20
    if pressed_keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= 20

    screen.fill(COLOR_WHITE)

    pygame.draw.circle(screen, COLOR_RED, (rect_x + 25, rect_y + 25), 25)

    pygame.display.flip()
    clock.tick(30)

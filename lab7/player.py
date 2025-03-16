import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 480))

COLOR_PINK = (255, 182, 193)
COLOR_LIGHT_BLUE = (173, 216, 230)
COLOR_LIGHT_GREEN = (144, 238, 144)
COLOR_LIGHT_PURPLE = (221, 160, 221)
COLOR_WHITE = (255, 255, 255)

font = pygame.font.Font(None, 50)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

_songs = [
    '/Users/rapiyatleukhan/Desktop/pp2/lab7/music/Chase%20Atlantic%20%E2%80%93%20Falling.mp3',
    '/Users/rapiyatleukhan/Desktop/pp2/lab7/music/dua-lipa-training-season.mp3',
    '/Users/rapiyatleukhan/Desktop/pp2/lab7/music/sabrina-carpenter-espresso.mp3',
    '/Users/rapiyatleukhan/Desktop/pp2/lab7/music/the-weeknd-dancing-in-the-flames.mp3'
]

def next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def previous_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

paused = False

def stopping():
    global paused
    paused = not paused
    if paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

clock = pygame.time.Clock()
FPS = 60

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            if event.key == pygame.K_LEFT:
                previous_song()
            if event.key == pygame.K_SPACE:
                stopping()
        if event.type == SONG_END:
            next_song()

    screen.fill(COLOR_PINK)

    draw_text("Music Player", 300, 20, COLOR_LIGHT_BLUE)
    draw_text("Now Playing:", 50, 100, COLOR_LIGHT_GREEN)
    draw_text(_songs[0].split('/')[-1], 50, 160, COLOR_WHITE)
    draw_text("Controls:", 50, 300, COLOR_LIGHT_PURPLE)
    draw_text("RIGHT - Next", 50, 360, COLOR_WHITE)
    draw_text("LEFT - Previous", 50, 400, COLOR_WHITE)
    draw_text("SPACE - Pause/Play", 50, 440, COLOR_WHITE)

    pygame.display.flip()
    clock.tick(FPS)

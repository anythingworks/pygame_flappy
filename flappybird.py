import pygame, time

black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 400
imageHeight = 110

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('flappy_bird_clone')
clock = pygame.time.Clock()

img = pygame.image.load('png/flappybird.png')

x = 50
y = 100
y_move = 0


def make_text_objs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msg_surface(text):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = make_text_objs(text, large_text)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    type_text_surf, typTextRect = make_text_objs('press any key to continue', small_text)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(type_text_surf, typTextRect)

    pygame.display.update()
    time.sleep(1)


def game_over():
    msg_surface('Kaboom!')


def bird(x, y, img):
    surface.blit(img, (x, y))

def init_globals():
    global x, y, y_move
    x = 50
    y = 100
    y_move = 0

def restart_game():
    if y > surfaceHeight - 110 or y < -70:
        msg_surface('Kaboom!')
        waiting_for_keypress = True
        while waiting_for_keypress:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting_for_keypress = False
                    init_globals()
                clock.tick()

def main():
    global x, y, y_move
    init_globals()

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.fill(black)
        bird(x, y, img)

        restart_game()

        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()

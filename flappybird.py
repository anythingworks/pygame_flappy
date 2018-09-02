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


def replay_or_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key

    return event.key


def makeTextObjs(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msg_surface(text):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, large_text)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    type_text_surf, typTextRect = makeTextObjs('press any key to continue', small_text)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(type_text_surf, typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit == None:
        clock.tick()


# main()

def gameOver():
    msg_surface('Kaboom!')
    quit()


def bird(x, y, image):
    surface.blit(img, (x, y))


def main():
    x = 50
    y = 100
    y_move = 0

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move

        surface.fill(black)
        bird(x, y, img)

        if y > surfaceHeight - 110 or y < -70:
            gameOver()

        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()

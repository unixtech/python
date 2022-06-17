import pygame


screen_size =  WIDTH, HEIGHT = 600, 600


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    fps = 3


    window_closed = False

    while not window_closed:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('FiraCode Retina', 18, True, False)
        text = font.render('Press Enter to start the game', True, (255, 255, 255))
        screen.blit(text, [180, HEIGHT // 2])

        for event in pygame.event.get():
            if even.type == pygame.QUIT:
                window_closed = True
        pygame.display.flip()
        clock.tick(fps)


    pygame.quit()

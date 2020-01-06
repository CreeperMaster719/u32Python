import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [255, 0, 0], [260, 200], 10, 0)
pygame.draw.circle(screen, [255, 255, 0], [380, 210], 15,
                   0)  # Just aded more circles. I nnoticed how they don't load in order.
pygame.draw.circle(screen, [0, 255, 0], [440, 220], 20, 0)
pygame.draw.circle(screen, [0, 255, 255], [200, 230], 25, 0)
pygame.draw.circle(screen, [0, 0, 255], [320, 240], 30, 0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

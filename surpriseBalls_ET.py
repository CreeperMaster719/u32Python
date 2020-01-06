import random

import pygame


class Ball:  # Allows for a LOT of stored variables.
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = []
        self.speedX = 0
        self.speedY = 0
        self.size = 0


def setBallPos():  #Cretes and randomizes ball.
    newBall = Ball()
    newBall.size = random.randint(5, 30)
    newBall.x = random.randrange(newBall.size, screenW - newBall.size)
    newBall.y = random.randrange(newBall.size, screenH - newBall.size)
    newBall.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    newBall.speedX = random.randint(1, 3)
    newBall.speedY = random.randint(1, 3)

    return newBall


pygame.init()
screenW = 1280
screenH = 720
size = [screenW, screenH]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Ball Pit")  #Sets program windoe nsme

clock = pygame.time.Clock()
ballList = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Space bar! Spawn a new ball.
            if event.key == pygame.K_SPACE:
                ball = setBallPos()
                ballList.append(ball)
    for ball in ballList:
        ball.x += ball.speedX
        ball.y += ball.speedY

        if ball.x >= screenW - ball.size or ball.x <= ball.size:
            ball.speedX *= -1
        if ball.y >= screenH - ball.size or ball.y <= ball.size:
            ball.speedY *= -1
    screen.fill((255, 255, 255))
    for ball in ballList:
        pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.size)  # Makes the ball each tick.
    clock.tick(120)  #Runs at 120fps! Super smooth!
    pygame.display.flip()
pygame.quit()

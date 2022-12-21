import pygame
from pygame.draw import *


pygame.init()

screen = pygame.display.set_mode((500, 500))
surf = pygame.Surface((500, 500))
surface_color = (255, 255, 255)

# здесь будут рисоваться фигуры
face_color = (255, 255, 0)
center = (250, 250)
circle_radius = 150
width = 0
surf.fill(surface_color)
screen.blit(surf, (0,0))
pygame.draw.circle(screen, face_color, center, circle_radius, width)

#eyes
pygame.draw.circle(screen, (255, 0, 0), (190, 200), 30, width)
pygame.draw.circle(screen, (255, 0, 0), (310, 200), 30, width)
pygame.draw.circle(screen, (0, 0, 0), (190, 200), 13, width)
pygame.draw.circle(screen, (0, 0, 0), (310, 200), 13, width)

#brows
pygame.draw.polygon(screen, (0, 0, 0), [(220,190), (225, 170), (225-170, 90), (225-179, 110)]) #left brow
pygame.draw.polygon(screen, (0, 0, 0), [(265,190), (260, 170), (295+150, 80), (300+150, 95)]) #right brow

#mouth
pygame.draw.rect(screen, (0, 0, 0), (180, 330, 140, 30))


clock = pygame.time.Clock()


clock.tick(30)

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()


# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
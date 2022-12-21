import pygame

pygame.init()

# create main display
screen = pygame.display.set_mode((500, 700))

# color palette
# black
# darkest_grey
# derker_grey
# medium_grey
# light_grey
# swamp_green
# burgundy
# yellow
# blue


# create surface for sky
sky = pygame.Surface((500, 700))
sky.fill((133, 129, 122))
screen.blit(sky, (0, 0))
pygame.display.update()

# create surface for ground
ground = pygame.Surface((500, 700))
ground.fill((0, 0, 0))
screen.blit(ground, (0, 300))
pygame.display.update()

### HOUSE ###
def house():
    # wall
    pygame.draw.rect(screen, (94, 79, 32), (25, 170, 270, 350))

    # roof
    pygame.draw.polygon(screen, (0, 0, 0), [(0, 170), (320, 170), (295, 135), (25, 135)])

    # windows
    def win(x, y):
        pygame.draw.rect(screen, (138, 172, 176), (x, y, 30, 150))

    win(40, 170)
    win(100, 170)
    win(175, 170)
    win(250, 170)

    # balcony
    pygame.draw.rect(screen, (51, 51, 51), (3, 300, 315, 30))
    pygame.draw.rect(screen, (51, 51, 51), (13, 250, 295, 20))

    def vertical_lines(x):
        pygame.draw.rect(screen, (51, 51, 51), (x, 260, 18, 40))

    vertical_lines(13)
    vertical_lines(55)
    vertical_lines(97)
    vertical_lines(139)
    vertical_lines(181)
    vertical_lines(223)
    vertical_lines(255)
    vertical_lines(290)

house()

# pipes
def thin_pipe(x, y):
    pygame.draw.rect(screen, (60, 60, 60), (x, y, 8, 70))

thin_pipe(50, 75)
thin_pipe(230, 85)
thin_pipe(170, 65)

pygame.draw.rect(screen, (60, 60, 60), (70, 79, 17, 70))

# down_windows
pygame.draw.rect(screen, (83, 19, 19), (60, 380, 55, 75))
pygame.draw.rect(screen, (83, 19, 19), (135, 380, 55, 75))
pygame.draw.rect(screen, (209, 213, 60), (210, 380, 55, 75))


# # create surface for sky
# sky = pygame.Surface((500, 700))
# sky.fill((133, 129, 122))
# screen.blit(sky, (0,0))
# pygame.display.update()
#
# # create surface for ground
# ground = pygame.Surface((500, 700))
# ground.fill((0, 0, 0))
# screen.blit(ground, (0,300))
# pygame.display.update()
#
#
# # wall
# pygame.draw.rect(screen, (94, 79, 32), (25, 170, 270, 350))
#
# # roof
# pygame.draw.polygon(screen, (0, 0, 0), [(0,170), (320, 170), (295, 135), (25, 135)])
#
# # windows
# def win(x, y):
#     pygame.draw.rect(screen, (138, 172, 176), (x, y, 30, 150))
#
# win(40, 170)
# win(100, 170)
# win(175, 170)
# win(250, 170)
#
# # balcony
# pygame.draw.rect(screen, (51, 51, 51), (3, 300, 315, 30))
# pygame.draw.rect(screen, (51, 51, 51), (13, 250, 295, 20))
#
# def vertical_lines(x):
#     pygame.draw.rect(screen, (51, 51, 51), (x, 260, 18, 40))
#
# vertical_lines(13)
# vertical_lines(55)
# vertical_lines(97)
# vertical_lines(139)
# vertical_lines(181)
# vertical_lines(223)
# vertical_lines(255)
# vertical_lines(290)
#
# #pipes
# def thin_pipe(x,y):
#     pygame.draw.rect(screen, (60, 60, 60), (x, y, 8, 70))
#
# thin_pipe(50, 75)
# thin_pipe(230, 85)
# thin_pipe(170, 65)
#
# pygame.draw.rect(screen, (60, 60, 60), (70, 79, 17, 70))
#
# #down_windows
# pygame.draw.rect(screen, (83, 19, 19), (60, 380, 55, 75))
# pygame.draw.rect(screen, (83, 19, 19), (135, 380, 55, 75))
# pygame.draw.rect(screen, (209, 213, 60), (210, 380, 55, 75))

#######

# ghost
img = pygame.image.load("D:\\test_repository\infa_2022_nikitina\infa_2022_nikitina\lab3\sourses\ghost.png")
img = pygame.transform.scale(img, (150, 200))
screen.blit(img, (330, 500))


def ghost(x, y, look):
    img = pygame.image.load("D:\\test_repository\infa_2022_nikitina\infa_2022_nikitina\lab3\sourses\ghost.png")
    img.set_alpha(100)
    img = pygame.transform.scale(img, (100, 150))

    if look == 'left':
        screen.blit(img, (x, y))
    elif look == 'right':
        img = pygame.transform.flip(img, True, False)
        screen.blit(img, (x, y))

ghost(200, 500, 'right')

# moon
pygame.draw.circle(screen, (246, 244, 213), (400, 70), 50)

# clouds
pygame.draw.ellipse(screen, (60, 60, 60, 5), (0,0, 300, 50))
pygame.draw.ellipse(screen, (40, 40, 40, 5), (100,40, 400, 50))


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
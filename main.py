import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import screenTypes as st


pygame.init()
pygame.display.set_caption("PaintXel")

window = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

screen = st.ScreenType("title")

running = True
while running:

    time_delta = clock.tick(60) / 1000
    mouse_cords = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))

    screen.draw(window, mouse_cords)

    pygame.display.update()

    clock.tick(60)

pygame.quit()


import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import screenTypes as st

pygame.init()
pygame.display.set_caption("PaintXel")

window = pygame.display.set_mode((900, 725))

clock = pygame.time.Clock()

screen_state = "title"
screen = st.ScreenType("title")

mouseClickTime = 0
mouseCoolDown = 0.2
click = False
slingleClick = False


running = True
while running:

    #Events and metadata
    time_delta = clock.tick(60) / 1000
    current_time = pygame.time.get_ticks() / 1000
    mouse_cords = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Manage click cooldown
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseClickTime + mouseCoolDown < current_time:
                click = True
                slingleClick = True
                mouseClickTime = current_time  
                print(mouse_cords)

        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    window.fill((255, 255, 255))


    newScreen = screen.draw(window, mouse_cords, click, slingleClick)
    if newScreen != screen_state:
        screen_state = newScreen
        screen = st.ScreenType(newScreen)

    pygame.display.update()

    clock.tick(60)

    slingleClick = False

pygame.quit()


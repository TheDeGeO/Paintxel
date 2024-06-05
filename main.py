import contextlib
with contextlib.redirect_stdout(None):
    import pygame

import screenTypes as st

# Initialize Pygame and set the window caption
pygame.init()
pygame.display.set_caption("PaintXel")

# Set the window size
window = pygame.display.set_mode((900, 725))

# Create a clock object to manage the game loop
clock = pygame.time.Clock()

# Initialize the screen state and screen object
screen_state = "title"
screen = st.ScreenType("title")

# Initialize variables for managing mouse clicks
mouseClickTime = 0
mouseCoolDown = 0.2
click = False
singleClick = False

# Main game loop
running = True
while running:

    # Get the time delta and current time
    time_delta = clock.tick(60) / 1000
    current_time = pygame.time.get_ticks() / 1000

    # Get the mouse coordinates
    mouse_cords = pygame.mouse.get_pos()

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Manage click cooldown
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseClickTime + mouseCoolDown < current_time:
                click = True
                singleClick = True
                mouseClickTime = current_time
                print(mouse_cords)

        if event.type == pygame.MOUSEBUTTONUP:
            click = False

    # Fill the window with white
    window.fill((255, 255, 255))

    # Draw the screen and check for a new screen state
    newScreen = screen.draw(window, mouse_cords, click, singleClick)
    if newScreen != screen_state:
        screen_state = newScreen
        screen = st.ScreenType(newScreen)

    # Update the display
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)

    # Reset the single click flag
    singleClick = False

# Quit Pygame
pygame.quit()
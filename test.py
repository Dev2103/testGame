import pygame

# -- Global constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank screen

size = (640,480)

screen = pygame.display.set_mode(size)

# --title if window
pygame.display.set_caption("Pong")
# -- exit game flag
done = False
sun_x = 40
sun_y = 100
# -- manages how fast screen refreshes
clock = pygame.time.Clock()


ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
x_padd = 0
y_padd = 220
### -- Game Loop
while not done:
    # -- User input and controls

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = true
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # - write logic that happens when you press the key
                    y_padd = y_padd - 20

                elif event.key == pygame.K_DOWN:
                    # - write logic that happens on key press here

                    y_padd = y_padd + 20    
                    #END If
                        
                #END If
            #Next event

    # -- Game logic goes after this comment
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    sun_x = sun_x + 5
    if x_val == 620: x_direction = x_direction * -1
    if y_val == 460: y_direction = y_direction * -1
    if x_val == 0: x_direction = x_direction * -1
    if y_val == 0: y_direction = y_direction * -1
    # -- screen background is black

    screen.fill(BLACK)

    # -- Draw here

    pygame.draw.rect(screen, BLUE, (x_val,y_val, ball_width,ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,15,60))

    # -- flip display to reveal new positions of objects

    pygame.display.flip()

    # -- the clock ticks over

    clock.tick(200)

#End while - end of game loop

pygame.quit()





import pygame
import random
import math

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
pygame.display.set_caption("Snow")

## -- define the class snow which is a sprit
class Snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
         # Call the sprite constructor
         super().__init__()
         # Create a sprite and fill it with colour
         self.image = pygame.Surface([width,height])
         self.image.fill(color)
         # Set the position of the sprite
         self.rect = self.image.get_rect()
         self.rect.x = random.randrange(0, 600)
         self.rect.y = random.randrange(0, 400)
    #End procedure
#End Class
         #-- exit game flag
done = False

# Create a list if the snow blocks

snow_group = pygame.sprite.Group()

# create a list of all sprites

all_sprites_group = pygame.sprite.Group()

# -- manages how fast screen refreshes

clock = pygame.time.Clock()

# create the snowflakes

number_of_flakes = 50 # we are creating 50 snowflakes

for x in range (number_of_flakes):

    my_snow = Snow(WHITE, 5, 5) # snowflakes are white with size 5 by 5 px

    snow_group.add (my_snow) # adds the new snowflake to the group of snowflakes

    all_sprites_group.add (my_snow) # adds it to the group of all Sprites

#Next x

### -- Game Loop
while not done:


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = true
            #End if
    #Next event

    # -- Game logic goes after this comment

    # -- screen background is black

    screen.fill(BLACK)

    # -- Draw here
    # -  screen background is BLACK
    screen.fill(BLACK)
# - draw here
    all_sprites_group.draw(screen)
    # -- User input and controls

   

    # -- flip display to reveal new positions of objects

    pygame.display.flip()

    # -- the clock ticks over

    clock.tick(60)

#End while - end of game loop

pygame.quit()



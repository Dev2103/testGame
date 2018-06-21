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
pygame.display.set_caption("Invaders")

## -- define the class snow which is a sprit
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # set the speed sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50,0)
    # class update function - runs for each pass through the loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
    #End procedure
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
         self.speed = 0
         super().__init__()
         self.image = pygame.Surface([width, height])
         self.image.fill(color)
         self.rect.x = 300
         self.rect.y = size[0] - height
    def update(self):
        self.rect.y = self.rect.y + self.speed
         
         
    
#End Class
         #-- exit game flag
done = False

# Create a list if the snow blocks

invader_group = pygame.sprite.Group()

# create a list of all sprites
pygame.draw.rect(screen, YELLOW, (0 ,0 ,10,10))
all_sprites_group = pygame.sprite.Group()

# -- manages how fast screen refreshes

clock = pygame.time.Clock()

# create the snowflakes

number_of_flakes = 10 # we are creating 50 snowflakes

for x in range (number_of_flakes):

    my_snow = Invader(BLUE, 10, 10 ,1) # snowflakes are white with size 5 by 5 px

    invader_group.add (my_snow) # adds the new snowflake to the group of snowflakes

    all_sprites_group.add (my_snow) # adds it to the group of all Sprites

#Next x

### -- Game Loop
while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            #End if
    #Next event

    # -- Game logic goes after this comment

    all_sprites_group.update()

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



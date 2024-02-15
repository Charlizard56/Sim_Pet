from Pet import Stats
from Draw import draw

#Notes
#Create Feeding
#Create Medication
#Fighting System
#Clean Up Text
#

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
#Set Font
basic_font = pygame.font.SysFont('Comic Sans MS', 30)

#Objects
pet = Stats("Pet",100,100,False)

#Pygame Setup
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sim Pet")
clock = pygame.time.Clock()
running = True
dt = 0
animation = 1
a_flip = True
paused = False
pause_time = 0

#Set Pet Position
pet.pos_x = screen.get_width()/2-pet.sprite_width/2
#Set Starting Frame
pet.sprite_width = pet.spr_frame[0]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #Animation
    pet.animate(animation,screen.get_width())

    #Draw
    draw(screen,pet.pos_x,pet.spr_size,pet.sprite_width,basic_font,pet)

    #Contols
    keys = pygame.key.get_pressed()
    #End Game
    if keys[pygame.K_ESCAPE]:
        running = False
        print("Game End")

    #Debug
    #Check Stats
    if keys[pygame.K_i]:
        pet.write_stats()

    #Test
    if keys[pygame.K_e]:
        pass

    #Auto
    pet.grow(animation)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60)/1000

    #Animation
    if animation >= 1:
        animation = 0
    animation += dt
    #print(f"Time: {animation}")

pygame.quit()







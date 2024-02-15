import pygame
from Pet import Stats
from Draw import draw
from Draw import pet_img
#Notes
#Create Sprite Slicer in Draw.py

pet = Stats("Billy",100,100,False)


# Press the green button in the gutter to run the script.

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

basic_font = pygame.font.SysFont('Comic Sans MS', 30)



screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
animation = 0
a_flip = True

#Set Pet Posistion
pet.pos_x = screen.get_width()/2-pet.sprite_width/2

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #Draw
    draw(screen,pet.pos_x,pet.spr_size,pet.sprite_width)
    my_font = basic_font.render(f"HP: {pet.hp}\nHunger: {pet.hunger}\nInjured: {pet.injured}", 0, "white")
    screen.blit(my_font, (10, 10))

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

    #Animation
    pet.animate(animation)

    #Test
    if keys[pygame.K_e]:
        #print("Change")
        pass

    #Auto
    pet.grow(animation)


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60)/1000

    #Animation
    if animation > 1:
        animation = 0
    animation += dt
    #print(f"Time: {animation}")

pygame.quit()







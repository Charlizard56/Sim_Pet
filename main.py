from Pet import Stats
from Draw import draw


#Notes
#Reconstruct text(Maybe into groups)
#Create Medication function
#Fighting System
#
#

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
#Set Font
basic_font = pygame.font.SysFont('Comic Sans MS', 30)

#Objects
pet = Stats("Pet",100,100,True)

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

        #Keyboard
        if event.type == pygame.KEYDOWN:
            #Feed
            if event.key == pygame.K_f:
                pet.feed(10)

            #Heal
            if event.key == pygame.K_h:
                pet.heal(20)

            #End Game
            if event.key == pygame.K_ESCAPE:
                running = False
                print("Game End")

        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                print(f"Left Mouse key was clicked: POS: {pygame.mouse.get_pos()}")



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    #Animation
    pet.animate(animation,screen.get_width())

    #Draw
    draw(screen,pet.pos_x,pet.spr_size,pet.sprite_width,basic_font,pet)

    #Auto
    pet.grow(animation)

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







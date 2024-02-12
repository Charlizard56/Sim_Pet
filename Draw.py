import pygame

#Sprites
pet_img = pygame.image.load("digimon.png")
pet_img = pygame.transform.scale(pet_img,(120,120))
pet_img = pygame.transform.flip(pet_img,1,0)

grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,(120,120))

def draw(_screen,_pet_x,_pet_y):
    #Set
    i = _screen.get_width()/100
    ground_width = 0
    a = 0

    # Grass
    try:
        while a < i:
            _screen.blit(grass_img, (ground_width, _screen.get_height() - grass_img.get_height()))
            a += 1
            ground_width += 100
            #print(a)
    except:
        print("Failed to draw ground.")
    #Pet
    _screen.blit(pet_img, (_screen.get_width()/2-pet_img.get_width(), _screen.get_height() - grass_img.get_height()-pet_img.get_height()/2))
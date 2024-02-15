import pygame

#Sprites
pet_img = pygame.image.load("d_sheet.png")
pet_spr = pet_img.get_width()/4-2


grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,(120,120))

def draw(_screen,_pet_x,_spr_size,_sprite_frame,_basic_font,_pet):
    #Set
    i = _screen.get_width()/100 #12.8
    ground_width = 0
    a = 0

    #Text
    my_font = _basic_font.render(f"HP: {_pet.hp}\nHunger: {_pet.hunger}\nInjured: {_pet.injured}", 0, "white")
    _screen.blit(my_font, (6, 0))

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

    _screen.blit(pet_img, (_pet_x,_screen.get_height()-120),(_sprite_frame, 0,_spr_size,_spr_size))

import pygame
#Recomended Size
r_spr_size = int(64)

#Sprites
#Pet
pet_img = pygame.image.load("d_sheet.png")
pet_spr = pet_img.get_width()/4-2

#HUD
burger_img = pygame.image.load("15_burger.png")
burger_img = pygame.transform.scale(burger_img,(r_spr_size,r_spr_size))
potion_img = pygame.image.load("Potion.png")
potion_img = pygame.transform.scale(potion_img,(r_spr_size,r_spr_size))

#Ground
grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img,(120,120))



def draw(_screen,_pet_x,_spr_size,_sprite_frame,_basic_font,_pet,_dead):
    #HUD
    _screen.blit(burger_img,(2,r_spr_size))
    _screen.blit(potion_img, (2, r_spr_size*2))

    #Set
    i = _screen.get_width()/100 #12.8
    ground_width = 0
    a = 0

    #Text
    pet_stats = _basic_font.render(f"{_pet.name} HP: {_pet.hp}\nFood: {_pet.food}\nInjured: {_pet.injured}", 0, "white")
    feed_text = _basic_font.render("F: Feed",0, 'white')
    heal_text = _basic_font.render("H: Heal", 0, 'white')

    #Draw Text
    _screen.blit(pet_stats, (6, 0))
    _screen.blit(feed_text,(r_spr_size,r_spr_size+10))
    _screen.blit(heal_text, (r_spr_size, r_spr_size*2 + 14))

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
    if _dead == False:
        _screen.blit(pet_img, (_pet_x,_screen.get_height()-120),(_sprite_frame, 0,_spr_size,_spr_size))

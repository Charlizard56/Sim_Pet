class Evolution:
    stage = 0

    def evolve(self):
        self.stage += 1

    def egg(self):
        pass

class Stats(Evolution):
    def __init__(self,name,hp,hunger,injured):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.injured = injured

    pos_x, pos_y = 200,0
    spr_size = 68

    #Movement
    speed = 4
    right = True

    #Sprite Animations
    sprite_width = 160
    a_flip = False

    def write_stats(self):
        print(f"Name: {self.name} HP: {self.hp},Hunger: {self.hunger}, Injured: {self.injured},Stage: {self.stage}Pos: {self.pos_x},{self.pos_y}")

    #Set
    def set_hunger(self,_add):
        self.hunger += _add
        self.write_stats()

    #Movement
    def move(self,_screen_width):
        if self.right:
            if self.pos_x < _screen_width - self.sprite_width - 100:
                self.pos_x += self.speed
                print(f"{self.right}")
            else:
                self.right = False
                print(self.right)
        if not self.right:
            if self.pos_x > 0 + self.sprite_width + 100:
                self.pos_x -= self.speed
                print(f"{self.right}")
            else:
                self.right = True
                print(self.right)

    #Animation
    def animate(self,_time):
        if (_time > 1):
            if self.a_flip:
                self.sprite_width = 160
                self.a_flip = False
            else:
                self.sprite_width = 180 / 2
                self.a_flip = True

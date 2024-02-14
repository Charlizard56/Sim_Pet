class Evolution:
    stage = 0

    def evolve(self):
        self.stage += 1

    def egg(self):
        pass

class Stats(Evolution):
    def __init__(self,name,hp,hunger,injured,sprite_width):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.injured = injured
        self.sprite_width = sprite_width

    pos_x, pos_y = 200,0
    spr_size = 68
    speed = 4
    right = True

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
    def animate(self):
        pass

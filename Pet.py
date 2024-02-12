class Evolution:
    stage = 0

    def evolve(self):
        self.stage += 1

class Stats(Evolution):
    def __init__(self,name,hp,hunger,injured):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.injured = injured

    pos_x, pos_y = 0,0
    spr_size = 64
    speed = 4

    def write_stats(self):
        print(f"Name: {self.name} HP: {self.hp},Hunger: {self.hunger}, Injured: {self.injured},Stage: {self.stage}")

    #Set
    def set_hunger(self,_add):
        self.hunger += _add
        self.write_stats()

    def set_pos_x(self,_x):
        self.pos_x = _x

    def set_pos_y(self,_y):
        self.pos_y = _y
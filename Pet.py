
class Evolution:
    stage = 0
    time = 0

    def evolve(self):
        self.stage += 1

class Stats(Evolution):
    def __init__(self,name,hp,hunger,injured):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.injured = injured

    #Pet Position
    pos_x, pos_y = 0,0

    #0-First Frame,1-Second Frame,etc.
    spr_frame = [0,66,118,160]
    #Size of individual sprite
    spr_size = 56

    #Movement
    speed = 4
    #Left and Right switch
    right = True

    #Sprite Animations
    #Total Width of Sprite Sheet
    sprite_width = 160
    a_flip = False

    def write_stats(self):
        print(f"Name: {self.name} HP: {self.hp},Hunger: {self.hunger}, Injured: {self.injured},Stage: {self.stage}Pos: {self.pos_x},{self.pos_y}")

    #Set


    #Movement
    def move(self,_screen_width):
        if self.right:
            if self.pos_x < _screen_width - self.spr_size:
                self.pos_x += self.speed
            else:
                self.right = False
        else:
            if self.pos_x > 0:
                self.pos_x -= self.speed
            else:
                self.right = True
        print(self.right)

    #Animation
    def animate(self,_time,_screen_width):
        if self.stage == 0:
            if (_time > 1):
                if self.a_flip:
                    self.sprite_width = self.spr_frame[0]
                    self.a_flip = False
                else:
                    self.sprite_width = self.spr_frame[1]
                    self.a_flip = True
        if self.stage == 1:
            #Out of combat
            if (_time > 1):
                if self.a_flip:
                    self.sprite_width = self.spr_frame[2]
                    self.a_flip = False
                else:
                    self.sprite_width = self.spr_frame[3]
                    self.a_flip = True
            #s trfelf.move(_screen_width)
    #Grow
    def grow(self,_time):
        #Egg
        if self.stage == 0:
            if self.time > 50:
                self.evolve()
                self.hunger = 20
                print(f"Evolved! Stage: {self.stage}")

        self.time += _time
        #print(f"Time: {self.time}/{50}")
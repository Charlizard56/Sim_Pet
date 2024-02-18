
class Stats:
    def __init__(self,_name,_hp,_hunger,_injured):
        self.name = _name
        self.hp = _hp
        self.hunger = _hunger
        self.injured = _injured

    dead = False

    #Evolution
    stage = 0
    clock = 0

    #Pet Position
    pos_x, pos_y = 0,0

    #0-First Frame,1-Second Frame,etc.
    spr_frame = [0,66,118,160]

    #Size of individual sprite
    spr_size = 56

    #Movement
    speed = 3
    #Left and Right switch
    right = True

    #Sprite Animations
    #Total Width of Sprite Sheet
    sprite_width = 160
    a_flip = False

    def write_stats(self):
        print(f"Name: {self.name} HP: {self.hp}| Hunger: {self.hunger}| Injured: {self.injured}| Stage: {self.stage}| X/Y:{self.pos_x},{self.pos_y}")

    #Care
    def feed(self,_filling):
        if self.stage > 0:
            if self.hunger < 100:
                self.hunger += _filling
                print("Fed")
                if self.hunger > 100:
                    self.hunger = 100
            else:
                print("Not Hungry")

    def heal(self,_power):
        if self.stage > 0:
            if self.injured:
                self.injured = False
                print("Healed")
            else:
                print("Not Injured")


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
            if _time > 1:
                if self.a_flip:
                    self.sprite_width = self.spr_frame[0]
                    self.a_flip = False
                else:
                    self.sprite_width = self.spr_frame[1]
                    self.a_flip = True
        if self.stage == 1:
            #Out of combat
            if _time > 1:
                if self.a_flip:
                    self.sprite_width = self.spr_frame[2]
                    self.a_flip = False
                else:
                    self.sprite_width = self.spr_frame[3]
                    self.a_flip = True
            #self.move(_screen_width)
    #Grow

    def evolve(self):
        self.stage += 1

    def death(self):
        if self.hp <= 0:
            self.dead = True
            print("your pet has died")

    def grow(self,_clock):
        if not self.dead:
            #Egg
            if self.stage == 0:
                if self.clock >= 60:
                    self.evolve()
                    self.hunger = 0
                    self.clock = 0
                    print(f"Evolved! Stage: {self.stage}")
            #Time
            if self.stage is not 0:
                if self.clock >= 200:
                    #Health
                    if self.hunger == 0 and self.hp != 0:
                        self.hp -= 5
                    #Hunger
                    if self.hunger != 0:
                        self.hunger -= 1
                    self.clock = 0
            self.death()
            self.clock += _clock
            #print(f"Time: {self.clock}/{60}")
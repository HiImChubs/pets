import pygame

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5
        
    def eat(self):
        if self.is_alive:
            print(self.name + " sips tea in his hood'")
            print(self.name + " says 'THAT SHIT GOOD!'")
            
        else:
            print(self.name + " is dead lmao.")
            
    def sleep(self):
        if self.is_alive:
            print(self.name + " is schleeep")
        else:
            print(self.name + " is always schleep in that grave lmao")
        

    def play(self):
        if self.is_alive:
            print(self.name + " kills that Yeet!")
        else:
            print(self.name + " hits that yeet in the grave")
    

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " memes on " + other.name +"!")
        print(other.name + " goes 'I'm dead lmao.'")
        other.is_alive = False

    def wakeup(self, other):
        print(self.name + " wakes " + other.name +"!")
        other.happiness += 1
        print(other.name + " is now woke af.")
        
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Bernard")
pet2 = Pet("Miguel")
pet3 = Pet("Enrique")

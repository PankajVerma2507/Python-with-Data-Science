 from random import randint as ri
import pgzrun

WIDTH = 800
HEIGHT = 500

# ALL THE CLASS LOGIC
class Player(Actor):

# override the default constructor
    def __init__(self,image,speed=5):
        pos =ri(0,WIDTH), ri(0,HEIGHT)
        super().__init__(image,pos)
        self.speed = speed

    def move(self):
        if keyboard.W:
            self.y -= self.speed
        elif keyboard.S:
            self.y += self.speed
        elif keyboard.A:
            self.x -= self.speed
            self.angle = 10
        elif keyboard.D:
            self.x += self.speed
            self.angle = -10
        else:
            self.angle = 0
    def check_boundary(self):
        if p.x < 0: # agar player left side se ja rha hai
            p.x = WIDTH # to right side se dikhne lge
        if p.x > WIDTH: # vice versa
            p.x = 0
        if p.y < 0:
            p.y = HEIGHT
        if p.y > HEIGHT:
            p.y = 0

        

# main game code

p = Player('ironman')
print(dir(p))

def draw():
    screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundary()

pgzrun.go()

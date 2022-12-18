from g2 import HEIGHT

WIDTH = 1000
HEIGHT = 500

p = Actor('chick',(100,100))
e = Actor("walrus",(500,200))

p.speed = 3
e.speed = 2

def player_movement():
    if keyboard.W:
        p.y -= p.speed
    if keyboard.S:
        p.y += p.speed
    if keyboard.A:
        p.x -=p.s
    if keyboard.D:
    p.x += p.s
    if p.x <


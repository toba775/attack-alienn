import pgzrun
import random

HEIGHT = 400
WIDTH = 400
points = 0
alien = Actor("alien")
t = "shoot"
def draw():
    screen.fill("black")
    alien.draw()
    screen.draw.text(t,(300,50))
    screen.draw.text(str(points),(50,350))

def on_mouse_down(pos):
    global t
    global points
    if alien.collidepoint(pos):
        alien.x = random.randint(0,400)
        alien.y = random.randint(0,400)
        t = "Good shot"
        points += 5
    else:
        t = "missed loser"
        points -= 50
    

pgzrun.go()
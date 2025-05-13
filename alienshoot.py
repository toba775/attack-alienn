import pgzrun
import random

HEIGHT = 400
WIDTH = 400
points = 0
alien = Actor("alien")
color = "black"
t = "shoot"
def draw():
    screen.fill(color)
    alien.draw()
    screen.draw.text(t,(300,50))
    screen.draw.text(str(points),(50,350))

def on_mouse_down(pos):
    global t
    global points
    global color
    if alien.collidepoint(pos):
        alien.x = random.randint(0,400)
        alien.y = random.randint(0,400)
        t = "Good shot"
        points += 5
        color = "green"
    else:
        t = "missed loser"
        points -= 50
        color = "red"
    

pgzrun.go()
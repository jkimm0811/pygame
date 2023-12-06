from random import randint
import pgzrun

WIDTH = 400
HEIGHT = 400

dots = []
lines = []

next_dot = 0

time_limit = 30
timer = 0
game_over = False

for dot in range(0,10):
    actor = Actor("dot")
    actor.pos = (randint(20, WIDTH - 20),randint(20, HEIGHT - 20))
    dots.append(actor)

def draw():
    screen.clear()
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number),(dot.pos[0],dot.pos[1]+12))
        dot.draw()
        number = number + 1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
    if next_dot == 10:
        screen.draw.text('Win',center=(200,130),color=("red"),fontsize=100)
        screen.draw.text(str(round(timer,3)),center=(200,230),color="red",fontsize=80)
        game_over=True
    else:
        screen.draw.text(str(round(timer,3)),topleft=(10,10),color="white",fontsize=19)
    if timer>=time_limit:
        screen.fill("black")
        screen.draw.text('GAME OVER',center=(200,200),color="red",fontsize=90)
        game_over=True

def on_mouse_down(pos):
    global next_dot
    global lines
    if next_dot<10:
        if dots[next_dot].collidepoint(pos):
            if next_dot:
                lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
                sounds.click.play()
            next_dot = next_dot + 1
        else:
            lines = []
            next_dot = 0

def update():
    global timer
    if next_dot!=10:
        timer=timer+1/60 

pgzrun.go()
        

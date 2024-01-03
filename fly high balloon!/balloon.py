from random import randint
import pgzrun

HEIGHT = 600
WIDTH = 800

game_over = False
score = 0
balloon_up = False
bird_up = True
make_flap=0


balloon = Actor('balloon')
bird = Actor('bird-up')
house = Actor('house')
tree = Actor('tree')

balloon.pos=400,300
bird.pos = randint(800,1600),randint(10,150)
house.pos = randint(800,1600),460
tree.pos = randint(800,1600),450

def draw():
    screen.blit('background',(0,0)) #이미지 
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('score='+str(score),(660,25),color='black',fontsize=37)
    else:
        screen.fill('black')
        screen.draw.text('Your score is '+str(score),center=(400,300),fontsize=80,color='red')

def on_mouse_down():
    global balloon_up
    balloon_up = True
    balloon.y = balloon.y-50

def on_mouse_up():
    global balloon_up
    balloon_up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = 'bird-down' #이미지는 액터에서의 설정과 다르게 바꿀 수 있음 
        bird_up = False
    else:
        bird.image = 'bird-up'
        bird_up = True

def update():
    global game_over, score, make_flap, bird
    if not game_over:
        if not balloon_up:
            balloon.y = balloon.y+1
        if house.right>0:
            house.x = house.x-2
        else:
            house.x = randint(800,1600)
            score=score+1
        #else는 바로 위에 있는 if에만 적용 (elif는 제외)
        if tree.right>0:
            tree.x = tree.x-2
        else:
            tree.x = randint(800,1600)
            score = score+1
        if bird.x>0:
            bird.x = bird.x - 4
            if make_flap==9:
                flap()
                make_flap=0
            else:
                make_flap=make_flap+1
        else:
            bird.x = randint(800,1600)
            bird.y = randint(10,150)
            score = score + 1
            make_flap = 0
        if balloon.collidepoint(tree.x,tree.y) or balloon.collidepoint(house.x,house.y) or balloon.collidepoint(bird.x,bird.y):
            game_over = True
        if balloon.bottom>560 or balloon.top<=0:
            game_over = True
            


        



pgzrun.go()

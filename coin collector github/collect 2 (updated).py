import pgzrun
from random import randint

WIDTH=600
HEIGHT=400

score=0
timeleft=10
game_over=False

fox=Actor("fox")
fox.pos=(100,100)

coin=Actor("coin")
coin.pos=(200,200)

def draw():
  screen.fill('saddle brown')
  fox.draw()
  coin.draw()
  screen.draw.text('Score='+str(score),color='white',fontsize=20,topleft=(10,10))
  screen.draw.text('Time:'+str(timeleft),topright=(WIDTH-10,10),color='white',fontsize=20)
  if game_over:
    screen.fill('red')
    screen.draw.text('Score='+str(score),topleft=(10,10),fontsize=60,color='white')

def place_coin():
  coin.x=randint(20,WIDTH-20)
  coin.y=randint(20,HEIGHT-20)

def update():
  global score
  
  if keyboard.left:
    fox.x=fox.x-2
  if keyboard.right:
    fox.x=fox.x+2
  if keyboard.up:
    fox.y=fox.y-2
  if keyboard.down:
    fox.y=fox.y+2

  if fox.colliderect(coin):
    score=score+100
    place_coin()

def update_timeleft():
    global timeleft
    global game_over

    if timeleft:  #0이 아닌 모든 숫자는 True
        timeleft=timeleft-1
    else:
        game_over=True

clock.schedule_interval(update_timeleft,1.0)


place_coin()
  
pgzrun.go()


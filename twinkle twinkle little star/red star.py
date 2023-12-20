import random
import pgzrun

WIDTH = 800
HEIGHT = 600
CENTER_X = 400
CENTER_Y = 300
CENTER = (400,300)
FINAL_LEVEL = 9
START_SPEED = 10 #1단계 일때 
COLORS = ['green','blue']
#unchanging variables - CAPITALIZE
#changing variables - lower case

game_over = False
game_complete = False
current_level = 1
stars = []
animations = []
score=0

def draw():
    global stars, current_level, game_over, game_complete, score
    screen.clear()
    screen.blit('space',(0,0))
    if game_over:
        display_message('Game Over','try again!')
    elif game_complete:
        display_message('You Won!','great job!')
    else:
        for star in stars:
            star.draw()
    screen.draw.text('score ='+str(score),fontsize=40,color='white',topleft=(20,20))

def update():
    global stars, current_level
    if len(stars)==0:
        stars = make_stars(current_level)

def make_stars(num_of_extra_stars):
    colors_to_create = get_colors_to_create(num_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(num_of_extra_stars):
    colors_to_create = ['red']
    for i in range(0,num_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create #출력이 아닌, 그 자리에 그 갚을 저장(save)한다 

def create_stars(colors_to_create):
    new_stars = []
    for x in colors_to_create:
        star = Actor(x+'-star')
        new_stars.append(star)
    return new_stars #new images holds actual images that were appended

def layout_stars(stars_to_layout):
    num_of_gaps = len(stars_to_layout)+1
    gap_size = WIDTH/num_of_gaps
    random.shuffle(stars_to_layout)
    for index,star in enumerate(stars_to_layout): #ENUMERATE
        star.x = (index+1)*gap_size

def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = START_SPEED - current_level #duration이 짧을수록 speed 올라감
        #duration은 정해준 곳까지 얼마나 걸려서 (얼마가 걸리든지 부드럽게 감) 갈지를 정해줌 
        star.anchor = ("center","bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        #on_finished는 지정해준 애니매이션 끝까지 갔을떄 (이 게임에서는 바닥에 닿았을때)
        animations.append(animation)

def display_message(x,y): #x는 heading text, y는 subheading text 
    screen.draw.text(x,fontsize=60,center=CENTER,color='white')
    screen.draw.text(y,fontsize=30,center=(CENTER_X,CENTER_Y+30),color='white')

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos): #여기서 pos(position)은 마우스에 위치를 말한다
    global stars, current_level
    for x in stars: #여기서 stars는 별의 대한 모든 정보를 담고 있다 (이미지, position, etc)
        if x.collidepoint(pos):
            if 'red' in x.image: #이 별의 이미지 안에 red라는 글자가 포함이 되어 있다면
                red_star_click()
            else: #1별을 클릭은 했지만 빨강이 아닐때, 
                handle_game_over()

def red_star_click():
    global stars, current_level, animations, game_complete, score
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level+1
        stars=[]
        animations=[]
    score=score+10

def stop_animations(list):
    for x in list:
        if x.running:
            x.stop()
                

pgzrun.go()

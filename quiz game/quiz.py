import pgzrun

WIDTH = 1280
HEIGHT = 720

qbox = Rect(0,0,820,240)
tbox = Rect(0,0,240,240)
abox1 = Rect(0,0,495,165)
abox2 = Rect(0,0,495,165)
abox3 = Rect(0,0,495,165)
abox4 = Rect(0,0,495,165)

qbox.move_ip(50,40) #topleft
tbox.move_ip(990,40)
abox1.move_ip(50,358)
abox2.move_ip(735,358)
abox3.move_ip(50,538)
abox4.move_ip(735,538)

q1 = ['What color is an apple?','yellow','black','red','purple',3]
q2 = ['What color is a banana?','yellow','orange','blue','red',1]
q3 = ['What color is a grape?','yellow','orange','purple','red',3]
q4 = ['What color is a strawberry?','yellow','orange','blue','red',4]
q5 = ['What color is a green apple?','yellow','green','blue','red',2]

aboxes = [abox1,abox2,abox3,abox4]
questions = [q1,q2,q3,q4,q5] #리스트 안에 리스트 

score=0
time_left=7
thisq = questions.pop(0) #0번째를 thisq가 가져가고, 리스트에서는 0번쨰가 지워짐 

def draw():
    screen.fill((140, 98, 58))
    screen.draw.filled_rect(qbox,(181, 146, 112))
    screen.draw.filled_rect(tbox,(242, 230, 218))
    for box in aboxes:
        screen.draw.filled_rect(box,(186, 171, 156))
    screen.draw.textbox(str(time_left),tbox) #뭘 적을지랑, 어디 (어느 박스)에 적을지
    screen.draw.textbox(thisq[0],qbox)  #q1의 첫번째 (질문)
    x=1
    for y in aboxes: #abox들이 들어있는 리스트(aboxes)에서 꺼내쓰기 (반복해서 안적게)
        screen.draw.textbox(thisq[x],y) 
        x=x+1

def gameover():
    global thisq,time_left,score
    message='Game over. You got %s questions correct.'%str(score) #게임 오비시, qbox의 표시될 문구 
    thisq=[message,'-','-','-','-',10]
    time_left=0

def correct_ans():
    global thisq,time_left,score
    score=score+1
    if questions: #questions안에 뭐라도 들어있으면 (empty list = false)
        thisq=questions.pop(0)
        time_left=7
    else: #questions가 비어있으면
        gameover()

def on_mouse_down(pos):
    x=1
    for box in aboxes:
        if box.collidepoint(pos):
            if x==thisq[5]:
                correct_ans()
            else:
                gameover()
        x=x+1

def t_reduce():
    global time_left
    if time_left:
        time_left=time_left-1
    else:
        gameover()

clock.schedule_interval(t_reduce,1.0)
    
pgzrun.go()

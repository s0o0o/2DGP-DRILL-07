from pico2d import *
from pygame.display import update
import random


# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습 결정
        self.image = load_image('grass.png')
    def update(self):
        pass

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,600), 90
        self.frame = random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100,100,self.x,self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass, team
    running = True
    grass = Grass() # 잔디를 찍어낸다. 생성한다.
    team = [Boy() for i in range (10)]

running = True

def update_world():
    grass.update() # 객체의 상태를 업데이트. 즉 시뮬레이션
    for boy in team:
        boy.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)



open_canvas()




# initialization code

reset_world() # 월드 초기화

# game main loop code
running = True
while running:
    # game logic
    handle_events()
    update_world() # 함수 먼저.. 상호작용을 시뮬레이션
    render_world() # 그 결과를 보여준다!


# finalization code

close_canvas()

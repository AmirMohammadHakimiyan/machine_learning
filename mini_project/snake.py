import random
import arcade
import time
# import main
class Fake(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("apple.png")
        self.center_x=x
        self.center_y=y
        self.width=1
        self.height=1
class Snake(arcade.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.center_x=random.randint(0,25)*20
        self.center_y=random.randint(0,25)*20
        self.width=20
        self.height=20
        self.change_x=0
        self.change_y=0
        self.speed=speed
        self.score=0
        self.body=[]
        self.c=0
        self.num=1
        self.time=0
        self.num_eat=0
        self.color=arcade.color.ORANGE
    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})
        if len(self.body)>self.score:
            self.body.pop(0)
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,20,20, arcade.color.AZURE_MIST)
        for i in self.body:
            self.num+=1
            if self.num%2==0:
                arcade.draw_rectangle_filled(i["x"],i["y"],20,20,arcade.color.AMARANTH_PINK)
            else:
                arcade.draw_rectangle_filled(i["x"],i["y"],20,20,arcade.color.AQUA)
    def Eat(self,food):
        self.num_eat+=1
        self.score+=food.score
        # if food.score>0:
        #     # self.body.append({"x":self.center_x-self.change_x*10,"y":self.center_y-self.change_y*10})
        #     ...
        # else :
        #     self.body.pop(0)
    def game_over(self):
        if self.score<0:
            if self.c==0:
                self.c=2
                self.time=time.time()
            self.over=arcade.load_texture("REN.png")
            arcade.draw_lrwh_rectangle_textured(0,0,600,600,self.over)
            self.speed=0



        for i in self.body:
            self.fake=Fake(i["x"]-10*self.change_x,i["y"]-10*self.change_y)
            if arcade.check_for_collision(self,self.fake):
                if self.body.index(i) > len(self.body)-3:
                    ...
                else:
                    self.score=-1
        if self.center_x>600 or self.center_x<0:
            self.score=-1
        if self.center_y>600 or self.center_y<0:
            self.score=-1

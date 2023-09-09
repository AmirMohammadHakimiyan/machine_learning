import pandas as pd
import arcade
import snake
import fruit

class Make_csv():
    def __init__(self):
 
        self.x_snake=[]
        self.y_snake=[]
        self.x_apple=[]
        self.y_apple=[]
        
        
        self.b1=[]
        self.b2=[]
        self.b3=[]
        self.b4=[]
       
        self.act1=[]
        self.act2=[]



    def run(self,x_snake,y_snake,x_apple,y_apple,b1,b2,b3,b4,
    act1,act2):
        
        self.x_snake.append(x_snake)
        self.y_snake.append(y_snake)
        self.x_apple.append(x_apple)
        self.y_apple.append(y_apple)
        self.b1.append(b1)
        self.b2.append(b2)
        self.b3.append(b3)
        self.b4.append(b4)
       
        self.act1.append(act1)
        self.act2.append(act2)
    
      
    def make(self):
        self.data={
        "x_snake":self.x_snake,
        "y_snake":self.y_snake,
        "x_apple":self.x_apple,
        "y_apple":self.y_apple,
        "b1":self.b1,
        "b2":self.b2,
        "b3":self.b3,
        "b4":self.b4,

       "act1":self.act1,
        "act2":self.act2}
        df=pd.DataFrame(self.data)
        df.to_csv("data.csv",index=False)



class Machin():
    def __init__(self):
        ...
    def farman(self,snake,food,b1,b2,b3,b4):
        n=1
        b=1
        c=1
        d=1

        
        if snake.center_y>food.center_y and abs(snake.center_y-food.center_y)>0:
            if b2>20 and n==1 and b==1 and d==1:
                snake.change_y=-1
                snake.change_x=0
                c=1
            elif b1>20 and b1-b3>0 and b2<=20:
                c=0
                snake.change_y=0
                snake.change_x=-1
            elif b3>20 and b2<=20:
                c=0
                snake.change_y=0
                snake.change_x=1
            else:
        
                c=1
        elif snake.center_y<food.center_y and abs(snake.center_y-food.center_y)>0:
            if b4>20 and n==1 and b==1 and c==1:
                d=1
                snake.change_y=1
                snake.change_x=0
            elif b4<=20 and b1>20 and b1-b3>0:
                d=0
                snake.change_y=0
                snake.change_x=-1
            elif b4<=20 and b3>20:
                d=0
                snake.change_y=0
                snake.change_x=1
            else:
  
                d=1

        elif abs(food.center_x-snake.center_x)>0 and snake.center_x<food.center_x:
            if b3>20 and b==1 and c==1 and d==1:
                n=1
                snake.change_x=1
                snake.change_y=0
            elif b4>20 and b4-b2>0 and b3<=20:
                n=0
                snake.change_x=0
                snake.change_y=1
            elif b2>20 and b3<=20:
                n=0
                snake.change_x=0
                snake.change_y=-1
            else:
  
                n=1
        elif abs(snake.center_x-food.center_x)>0 and snake.center_x>food.center_x:
            if b1>20 and n==1 and c==1 and d==1:
  
                b=1
                snake.change_x=-1
                snake.change_y=0
            elif b4>20 and b1<=20 and b4-b2>0:
                b=0
                snake.change_x=0
                snake.change_y=1
            elif b2>20 and b1<=20:
                b=0
                snake.change_x=0
                snake.change_y=-1
            else:
                b=1
         
       
        elif snake.center_y>food.center_y and abs(snake.center_y-food.center_y)>0:
            if b2>20 and n==1 and b==1 and d==1:
                snake.change_y=-1
                snake.change_x=0
                c=1


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height=600, title="snake")
        arcade.set_background_color(arcade.color.WARM_BLACK)
        self.number={"0":"scr/0.png","1":"scr/1.png","2":"scr/2.png","3":"scr/3.png","4":"scr/4.png","5":"scr/5.png","6":"scr/6.png","7":"scr/7.png","8":"scr/8.png","9":"scr/9.png"}
        self.mushroom=fruit.Mushroom("scr/mushroom.png")
        self.bg=arcade.load_texture("scr/BG.png")
        self.apple=fruit.Apple("scr/apple.png")
        self.pear=fruit.Pear("scr/pear.png")
        self.snake=snake.Snake(20)
        self.make_csv=Make_csv()
        self.machin=Machin()
        self.counter=0
        self.act1=[]
        self.act2=[]
        self.x_snake=[]
        self.y_snake=[]
        self.x_apple=[]
        self.y_apple=[]
        self.b1=[]
        self.b2=[]
        self.b3=[]
        self.b4=[]
        self.all_score=[]
    def on_draw(self):
        arcade.start_render()
        self.mushroom.draw()
        self.pear.draw()
        self.apple.draw()
        self.snake.draw()
        for i in self.snake.body:
            self.fake=snake.Fake(i["x"]-10*self.snake.change_x,i["y"]-10*self.snake.change_y)
            if arcade.check_for_collision(self.snake,self.fake):
                if self.snake.body.index(i) > len(self.snake.body)-3:
                    ...
                else:
                    self.snake.score=-1
        if self.snake.center_x>600 or self.snake.center_x<0:
            self.snake.score=-1
        if self.snake.center_y>600 or self.snake.center_y<0:
            self.snake.score=-1

        if self.snake.score<0:
            self.all_score.append(self.snake.score)
            del self.snake
            self.snake=snake.Snake(20)


            

        if self.snake.score>=0:
            self.n=str(self.snake.score).replace("",",")
            self.m=self.n.split(",")
            for i in self.m:
                if i !="":
                    self.shape=arcade.load_texture(self.number[i])
                    arcade.draw_lrwh_rectangle_textured(self.m.index(i)*40,0,40,40,self.shape)
        arcade.finish_render()


                
    def on_update(self, delta_time: float):

        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.Eat(self.apple)
            self.counter+=1
            del self.apple
            if self.counter%2==0:
                self.apple=fruit.Apple("scr/apple.png")
            else:
                self.apple=fruit.Apple("scr/apple.png")
        if arcade.check_for_collision(self.snake,self.pear):
            self.snake.Eat(self.pear)
            del self.pear
            self.pear=fruit.Pear("scr/pear.png")
        if arcade.check_for_collision(self.snake,self.mushroom):
            self.snake.Eat(self.mushroom)
            del self.mushroom
            self.mushroom=fruit.Mushroom("scr/mushroom.png")
        self.b1=400
        self.b2=400
        self.b3=400
        self.b4=400

        for i in self.snake.body:
            if i["y"]==self.snake.center_y and self.snake.center_x>i["x"]:
                self.b1=abs(i["x"]-self.snake.center_x)
            if i["x"]==self.snake.center_x and self.snake.center_y>i["y"]:
                self.b2=abs(i["y"]-self.snake.center_y)
            if i["y"]==self.snake.center_y and self.snake.center_x<i["x"]:
                self.b3=abs(i["x"]-self.snake.center_x)                
            if i["x"]==self.snake.center_x and self.snake.center_y<i["y"]:
                self.b4=abs(i["y"]-self.snake.center_y)

        




        
        self.counter+=1
     
        change_x_old=self.snake.change_x
        change_y_old=self.snake.change_y

        self.machin.farman(self.snake,self.apple,self.b1,self.b2,self.b3,self.b4)
            

        
        
        if change_x_old==self.snake.center_x or change_y_old==self.snake.change_y:
            ...
        else:
            self.make_csv.run(self.snake.center_x,self.snake.center_y,self.apple.center_x,self.apple.center_y,
self.b1,self.b2,self.b3,self.b4,self.snake.change_x,self.snake.change_y)
        if self.counter%50==0:
            self.make_csv.run(self.snake.center_x,self.snake.center_y,self.apple.center_x,self.apple.center_y,
self.b1,self.b2,self.b3,self.b4,self.snake.change_x,self.snake.change_y)
  
window=Game()
arcade.run()

window.make_csv.make()











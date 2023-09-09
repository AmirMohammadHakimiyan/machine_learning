import tensorflow as tf
import numpy as np
import time 
import arcade
import snake
import fruit

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
        self.model=tf.keras.models.load_model("weights/neural_network.h5")
        self.counter=0
    def on_draw(self):
        arcade.start_render()
        self.mushroom.draw()
        self.pear.draw()
        self.apple.draw()
        self.snake.draw()
        self.snake.game_over()
        if int(time.time()-self.snake.time)==1:
            exit(0)
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

        




        
        
     
        

        x=np.array([[self.snake.center_x,self.snake.center_y,self.apple.center_x,self.apple.center_y,
self.b1,self.b2,self.b3,self.b4]])
        y=self.model.predict(x)
        if np.argmax(y)==0:
            self.snake.change_x=-1
            self.snake.change_y=0
        elif  np.argmax(y)==1:
            self.snake.change_x=0
            self.snake.change_y=-1
        elif np.argmax(y)==2:
            self.snake.change_x=1
            self.snake.change_y=0
        elif np.argmax(y)==3:
            self.snake.change_x=0
            self.snake.change_y=1

        
        
        
        
      
        
window=Game()
arcade.run()
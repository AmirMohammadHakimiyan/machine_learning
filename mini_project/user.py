import time 
import arcade
import snake
import fruit

   

import numpy as np
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height=600, title="snake")
        arcade.set_background_color(arcade.color.WARM_BLACK)
        self.number={"0":"0.png","1":"1.png","2":"2.png","3":"3.png","4":"4.png","5":"5.png","6":"6.png","7":"7.png","8":"8.png","9":"9.png"}
        self.mushroom=fruit.Mushroom("mushroom.png",0)
        self.bg=arcade.load_texture("BG.png")
        self.apple=fruit.Apple("apple.png",0)
        self.pear=fruit.Pear("pear.png",0)
        self.snake=snake.Snake(10)
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

    def on_key_press(self, symbol: int, modifiers: int):
        
        
        if symbol==arcade.key.UP:
            self.snake.change_y=1
            self.snake.change_x=0
                
        if symbol==arcade.key.DOWN:
                
            self.snake.change_y=-1
            self.snake.change_x=0
             
        if symbol==arcade.key.RIGHT:
                
            self.snake.change_x=1
            self.snake.change_y=0
               
        if symbol==arcade.key.LEFT:
                
            self.snake.change_x=-1
            self.snake.change_y=0
              
                
    def on_update(self, delta_time: float):
        
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.Eat(self.apple)
            self.counter+=1
            del self.apple
            if self.counter%2==0:
                self.apple=fruit.Apple("apple.png",0)
            else:
                self.apple=fruit.Apple("apple.png",1)
        if arcade.check_for_collision(self.snake,self.pear):
            self.snake.Eat(self.pear)
            del self.pear
            self.pear=fruit.Pear("pear.png",1)
        if arcade.check_for_collision(self.snake,self.mushroom):
            self.snake.Eat(self.mushroom)
            del self.mushroom
            self.mushroom=fruit.Mushroom("mushroom.png",1)
        
        
window=Game()
arcade.run()
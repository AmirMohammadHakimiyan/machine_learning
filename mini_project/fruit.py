import random
import arcade
class Fruit(arcade.Sprite):
    def __init__(self,pic,b):
        super().__init__(pic)
        if b==0:
            self.center_x=random.randint(0,600)//20*20
        else:
            self.center_x=random.randint(0,600)//20*20
        self.center_y=random.randint(0,600)//20*20
class Apple(Fruit):
    def __init__(self,p,b):
        super().__init__(p,b)
        self.score=1
        self.height=20
        self.width=20


class Pear(Fruit):
    def __init__(self,p,b):
        super().__init__(p,b)
        self.score=1
        self.height=20
        self.width=20



class Mushroom(Fruit):
    def __init__(self,pic,b):
        super().__init__(pic,b)
        self.score=1
        self.height=20
        self.width=20

import pandas as pd

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
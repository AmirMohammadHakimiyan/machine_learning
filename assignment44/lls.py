import numpy as np
from scipy import stats
class LLS():
    def __init__(self,x,y):
        self.x_train=x
        self.y_train=y
    def fit(self):
        self.slope,self.intercept,self.r,self.p,self.std_err=stats.linregress(self.x_train,self.y_train)
        self.e_line=self.x_train*self.slope+self.intercept
    def predict(self,X):
        Y=[]
        for x in X:
            y=x*self.slope+self.intercept
            Y.append(y)
        return Y
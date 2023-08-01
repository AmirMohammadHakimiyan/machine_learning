import random
import time
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

_, ax_1=plt.subplots(1,1)

class Perceptron ():
    def __init__(self,w,b):
        self.w = w
        self.b = b
    def fit (self, X_train, Y_train):
        self.X_train= X_train
        self.Y_train= Y_train
        loss = []
        for y in range(50):
            for i in range(X_train.shape[0]):
                y_pred = X_train[i] * self.w + self.b
                error = Y_train[i] - y_pred
                self.w = self.w + (error * X_train[i] * 0.001)
                self.b = self.b + (error * 0.1)
                er = np.mean(np.abs(error))
                loss.append(er)

        return self.w ,self.b

                # ax_1.clear()
                # ax_1.scatter(X_train,Y_train,color="blue")
                # ax_1.plot(X_train,X_train*self.w+self.b)
                # plt.pause(0.1)

    def predict(self, X_test):

        return X_test*self.w+self.b



    def evaluate (self,X_test, y_test):
        pred = X_test*self.w+self.b
        error = np.sum((y_test - pred)/len(y_test))
        return error

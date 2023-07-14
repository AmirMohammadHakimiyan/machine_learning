import numpy as np
class Knn ():
    def __init__(self,k):
        self.k=k

    def fit (self,x,y):
        self.x_train=x
        self.y_train=y

    def euclidean_distance(self,x1,x2):
        return np.sqrt(np.sum((x1-x2)**2, axis=1))

    def predict (self, x):
        Y = []

        for i in x :
            
            distances = self.euclidean_distance(i, self.x_train)
            nearest_neighbors = np.argsort(distances)[0:self.k]
            result = np.bincount(self.y_train[nearest_neighbors])
            y = np.argmax(result)
            Y.append(y)
        return Y

    def score (self, x,y):
        self.y_test = y
        self.y_pred = self.predict(x)
        accuracy = np.sum(self.y_pred == self.y_test)
        return 100*accuracy/len(self.y_test)


    


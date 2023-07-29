import numpy as np

class LinearLeastSsquare :
    def __init__(self):
        
        self.w = None

    def fit (self, x_train, y_train):

        self.w = np.linalg.inv(x_train.T @ x_train) @ x_train.T @ y_train # (x.T * x)^-1 * x.T * y

    def predict(self, x_test):

        self.pred = x_test @ self.w

        return self.pred

    def evaluate (self, x_test, y_test, metric):
        y_pred = self.predict(x_test)

        if metric == "mae":
            loss = np.sum(np.abs(y_test - y_pred)) / len(y_test)
        if metric == "mse":
            loss = np.sum((y_test - y_pred) ** 2) / len(y_test)

        return loss
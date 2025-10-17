import numpy as np
from mesa import Agent

class PerceptronAgent(Agent):
    def __init__(self, unique_id, model, learning_rate=0.1):
        super().__init__(unique_id, model)
        self.weights = np.random.uniform(-1, 1, 2)
        self.bias = np.random.uniform(-1, 1)
        self.learning_rate = learning_rate

    def predict(self, x):
        return 1 if np.dot(self.weights, x) + self.bias >= 0 else -1

    def train(self, x, y_true):
        y_pred = self.predict(x)
        if y_pred != y_true:
            self.weights += self.learning_rate * (y_true - y_pred) * x
            self.bias += self.learning_rate * (y_true - y_pred)


class DataPoint(Agent):
    def __init__(self, unique_id, model, x, y, label):
        super().__init__(unique_id, model)
        self.x = x
        self.y = y
        self.label = label
        self.predicted = None
        self.correct = None
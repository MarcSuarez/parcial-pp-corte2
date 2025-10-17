import numpy as np
from mesa import Model
from mesa.time import BaseScheduler
from mesa.datacollection import DataCollector
from .perceptron_agent import PerceptronAgent, DataPoint

class PerceptronModel(Model):
    def __init__(self, n_points=100, learning_rate=0.1, epochs=10):
        super().__init__()
        self.schedule = BaseScheduler(self)
        self.n_points = n_points
        self.epochs = epochs
        self.current_point = 0
        
        # Crear perceptrón
        self.perceptron = PerceptronAgent(0, self, learning_rate)
        
        # Generar línea separadora: y = mx + c
        self.m = np.random.uniform(-2, 2)
        self.c = np.random.uniform(-2, 2)
        
        # Generar datos
        self.points = []
        for i in range(n_points):
            x = np.random.uniform(-5, 5)
            y = np.random.uniform(-5, 5)
            label = 1 if y >= self.m * x + self.c else -1
            point = DataPoint(i+1, self, x, y, label)
            self.points.append(point)
            self.schedule.add(point)
        
        # Índices de entrenamiento
        self.train_indices = []
        for _ in range(epochs):
            indices = list(range(n_points))
            np.random.shuffle(indices)
            self.train_indices.extend(indices)
        
        self.datacollector = DataCollector(
            model_reporters={"Precisión": lambda m: m.get_accuracy()}
        )
        self.running = True

    def step(self):
        if self.current_point >= len(self.train_indices):
            self.running = False
            return
        
        # Entrenar con un punto
        idx = self.train_indices[self.current_point]
        point = self.points[idx]
        x_data = np.array([point.x, point.y])
        self.perceptron.train(x_data, point.label)
        
        # Actualizar predicciones
        for p in self.points:
            x = np.array([p.x, p.y])
            p.predicted = self.perceptron.predict(x)
            p.correct = (p.predicted == p.label)
        
        self.current_point += 1
        self.datacollector.collect(self)

    def get_accuracy(self):
        if not self.points:
            return 0
        correct = sum(1 for p in self.points if p.correct)
        return correct / len(self.points) * 100

    def get_summary(self):
        acc = self.get_accuracy()
        w = self.perceptron.weights
        b = self.perceptron.bias
        step = f"{self.current_point}/{len(self.train_indices)}"
        return f"Paso: {step} | Precisión: {acc:.1f}% | Pesos: [{w[0]:.2f}, {w[1]:.2f}] | Bias: {b:.2f}"
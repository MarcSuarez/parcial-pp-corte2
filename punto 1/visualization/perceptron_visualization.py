from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter
from models.perceptron_model import PerceptronModel

chart = ChartModule(
    [{"Label": "Precisión", "Color": "blue"}],
    data_collector_name="datacollector"
)

model_params = {
    "n_points": UserSettableParameter("slider", "Número de puntos", 100, 20, 300, 10),
    "learning_rate": UserSettableParameter("slider", "Tasa de aprendizaje", 0.1, 0.01, 1.0, 0.01),
    "epochs": UserSettableParameter("slider", "Número de iteraciones", 10, 1, 50, 1)
}

server = ModularServer(
    PerceptronModel,
    [chart],
    "Simulador de Perceptrón",
    model_params
)
server.port = 8521
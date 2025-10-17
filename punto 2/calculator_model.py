from mesa import Model
from mesa.time import RandomActivation
from io_agent import IOAgent
from operation_agents import (
    SumAgent,
    SubtractionAgent,
    MultiplicationAgent,
    DivisionAgent,
    PowerAgent
)


class CalculatorModel(Model):
    """Modelo principal de la calculadora"""
    
    def __init__(self):
        super().__init__()
        self.schedule = RandomActivation(self)
        
        # Crear agentes
        self.io_agent = IOAgent(0, self)
        self.sum_agent = SumAgent(1, self)
        self.sub_agent = SubtractionAgent(2, self)
        self.mul_agent = MultiplicationAgent(3, self)
        self.div_agent = DivisionAgent(4, self)
        self.pow_agent = PowerAgent(5, self)
        
        # Agregar agentes al scheduler
        self.schedule.add(self.io_agent)
        self.schedule.add(self.sum_agent)
        self.schedule.add(self.sub_agent)
        self.schedule.add(self.mul_agent)
        self.schedule.add(self.div_agent)
        self.schedule.add(self.pow_agent)
        
    def calculate(self, expression: str) -> float:
        """Calcula el resultado de una expresión"""
        try:
            result = self.io_agent.parse_expression(expression)
            return result
        except Exception as e:
            raise ValueError(f"Error al calcular: {str(e)}")

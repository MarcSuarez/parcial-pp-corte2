from mesa import Agent
from typing import Dict
from messages import Message, MessageType


class OperationAgent(Agent):
    """Agente base para operaciones aritméticas"""
    
    def __init__(self, unique_id, model, operation_symbol):
        super().__init__(unique_id, model)
        self.operation_symbol = operation_symbol
        self.inbox = []
        self.results = {}
        
    def receive_message(self, message: Message):
        """Recibe un mensaje de otro agente"""
        self.inbox.append(message)
        
    def send_message(self, receiver_id: int, msg_type: MessageType, content: Dict):
        """Envía un mensaje a otro agente"""
        message = Message(self.unique_id, receiver_id, msg_type, content)
        receiver = self.model.schedule.agents[receiver_id]
        receiver.receive_message(message)
        
    def calculate(self, operand1: float, operand2: float) -> float:
        """Método abstracto para realizar el cálculo"""
        raise NotImplementedError
        
    def step(self):
        """Procesa mensajes en cada paso"""
        while self.inbox:
            message = self.inbox.pop(0)
            
            if message.msg_type == MessageType.CALCULATE:
                op1 = message.content['operand1']
                op2 = message.content['operand2']
                request_id = message.content['request_id']
                
                result = self.calculate(op1, op2)
                
                # Enviar resultado de vuelta
                self.send_message(
                    message.sender_id,
                    MessageType.RESULT,
                    {'result': result, 'request_id': request_id}
                )


class SumAgent(OperationAgent):
    """Agente para operaciones de suma"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, '+')
        
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 + operand2


class SubtractionAgent(OperationAgent):
    """Agente para operaciones de resta"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, '-')
        
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 - operand2


class MultiplicationAgent(OperationAgent):
    """Agente para operaciones de multiplicación"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, '*')
        
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 * operand2


class DivisionAgent(OperationAgent):
    """Agente para operaciones de división"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, '/')
        
    def calculate(self, operand1: float, operand2: float) -> float:
        if operand2 == 0:
            raise ValueError("División por cero no permitida")
        return operand1 / operand2


class PowerAgent(OperationAgent):
    """Agente para operaciones de potencia"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model, '^')
        
    def calculate(self, operand1: float, operand2: float) -> float:
        return operand1 ** operand2
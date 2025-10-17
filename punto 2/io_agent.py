from mesa import Agent
from messages import Message, MessageType
from typing import List
import re


class IOAgent(Agent):
    """Agente de Entrada/Salida - Coordinador principal"""
    
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.inbox = []
        self.pending_requests = {}
        self.request_counter = 0
        self.final_result = None
        
    def receive_message(self, message: Message):
        """Recibe mensajes de otros agentes"""
        self.inbox.append(message)
        
    def parse_expression(self, expression: str) -> float:
        """Analiza y evalúa la expresión matemática"""
        # Eliminar espacios
        expression = expression.replace(' ', '')
        
        # Evaluar la expresión usando precedencia de operadores
        return self.evaluate_expression(expression)
        
    def evaluate_expression(self, expr: str) -> float:
        """Evalúa la expresión respetando la precedencia de operadores"""
        # Reemplazar ^ por ** para potencias
        expr = expr.replace('^', '**')
        
        # Tokenizar la expresión
        tokens = re.findall(r'\d+\.?\d*|\*\*|[+\-*/()]', expr)
        
        # Convertir a notación postfija (Reverse Polish Notation)
        postfix = self.infix_to_postfix(tokens)
        
        # Evaluar la expresión postfija usando agentes
        result = self.evaluate_postfix(postfix)
        
        return result
        
    def infix_to_postfix(self, tokens: List[str]) -> List[str]:
        """Convierte notación infija a postfija (algoritmo Shunting Yard)"""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
        right_associative = {'**'}
        
        output = []
        operator_stack = []
        
        for token in tokens:
            if re.match(r'\d+\.?\d*', token):  # Número
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()  # Eliminar '('
            elif token in precedence:
                while (operator_stack and 
                       operator_stack[-1] != '(' and
                       operator_stack[-1] in precedence and
                       (precedence[operator_stack[-1]] > precedence[token] or
                        (precedence[operator_stack[-1]] == precedence[token] and 
                         token not in right_associative))):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        
        while operator_stack:
            output.append(operator_stack.pop())
            
        return output
        
    def evaluate_postfix(self, postfix: List[str]) -> float:
        """Evalúa expresión postfija usando agentes"""
        stack = []
        
        for token in postfix:
            if re.match(r'\d+\.?\d*', token):  # Número
                stack.append(float(token))
            else:  # Operador
                if len(stack) < 2:
                    raise ValueError("Expresión inválida")
                    
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                # Determinar qué agente usar
                agent_map = {
                    '+': 1,  # SumAgent
                    '-': 2,  # SubtractionAgent
                    '*': 3,  # MultiplicationAgent
                    '/': 4,  # DivisionAgent
                    '**': 5  # PowerAgent
                }
                
                agent_id = agent_map.get(token)
                if agent_id is None:
                    raise ValueError(f"Operador no soportado: {token}")
                
                # Solicitar cálculo al agente
                result = self.request_calculation(agent_id, operand1, operand2)
                stack.append(result)
        
        if len(stack) != 1:
            raise ValueError("Expresión inválida")
            
        return stack[0]
        
    def request_calculation(self, agent_id: int, op1: float, op2: float) -> float:
        """Solicita un cálculo a un agente específico"""
        self.request_counter += 1
        request_id = self.request_counter
        
        # Crear mensaje
        message = Message(
            self.unique_id,
            agent_id,
            MessageType.CALCULATE,
            {
                'operand1': op1,
                'operand2': op2,
                'request_id': request_id
            }
        )
        
        # Enviar mensaje
        target_agent = self.model.schedule.agents[agent_id]
        target_agent.receive_message(message)
        
        # Ejecutar un paso del agente para procesar
        target_agent.step()
        
        # Esperar respuesta (simulación síncrona)
        self.step()
        
        # Obtener resultado
        if request_id in self.pending_requests:
            result = self.pending_requests.pop(request_id)
            return result
        else:
            raise RuntimeError("No se recibió respuesta del agente")
        
    def step(self):
        """Procesa mensajes entrantes"""
        while self.inbox:
            message = self.inbox.pop(0)
            
            if message.msg_type == MessageType.RESULT:
                request_id = message.content['request_id']
                result = message.content['result']
                self.pending_requests[request_id] = result

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Any


class MessageType(Enum):
    """Tipos de mensajes entre agentes"""
    CALCULATE = "calculate"
    RESULT = "result"
    REQUEST = "request"


@dataclass
class Message:
    """Mensaje entre agentes"""
    sender_id: int
    receiver_id: int
    msg_type: MessageType
    content: Dict[str, Any]
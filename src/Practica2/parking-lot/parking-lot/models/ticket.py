from datetime import datetime
from enum import Enum

class EstadoTicket(Enum):
    ACTIVO = "ACTIVO"
    CERRADO = "CERRADO"

class Ticket:
    def __init__(self, id_ticket: int, vehiculo, espacio):
        self.id_ticket = id_ticket
        self.vehiculo = vehiculo
        self.espacio = espacio
        self.hora_entrada = datetime.now()
        self.hora_salida = None
        self.estado = EstadoTicket.ACTIVO

    def cerrar(self):
        # guarda hora de fin
        self.hora_salida = datetime.now()
        self.estado = EstadoTicket.CERRADO
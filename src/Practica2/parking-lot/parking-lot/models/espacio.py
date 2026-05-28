from enum import Enum

class TipoEspacio(Enum):
    AUTO = "AUTO"
    MOTO = "MOTO"
    CUALQUIERA = "CUALQUIERA"

class EspacioParqueo:
    def __init__(self, id_espacio: str, permitido: TipoEspacio):
        self.id_espacio = id_espacio
        self.permitido = permitido
        self.ocupado = False
        self.vehiculo_actual = None

    def ocupar(self, vehiculo):
        # marca lugar como lleno
        self.ocupado = True
        self.vehiculo_actual = vehiculo

    def liberar(self):
        # limpia el lugar
        self.ocupado = False
        self.vehiculo_actual = None
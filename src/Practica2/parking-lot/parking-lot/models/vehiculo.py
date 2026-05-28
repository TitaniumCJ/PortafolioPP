from dataclasses import dataclass
from enum import Enum

class TipoVehiculo(Enum):
    AUTO = "AUTO"
    MOTO = "MOTO"

@dataclass
class Vehiculo:
    placa: str
    tipo: TipoVehiculo

class Auto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.AUTO)

class Moto(Vehiculo):
    def __init__(self, placa: str):
        super().__init__(placa, TipoVehiculo.MOTO)
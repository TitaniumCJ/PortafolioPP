from abc import ABC, abstractmethod

class PoliticaTarifa(ABC):
    @abstractmethod
    def calcular(self, horas: float, tipo_vehiculo: str) -> float:
        pass

class TarifaPorHora(PoliticaTarifa):
    def calcular(self, horas: float, tipo_vehiculo: str) -> float:
        # costo por tipo de vehiculo
        precio = 20.0 if tipo_vehiculo == "AUTO" else 10.0
        return horas * precio

class TarifaPlana(PoliticaTarifa):
    def calcular(self, horas: float, tipo_vehiculo: str) -> float:
        # cobro fijo sin importar tiempo
        return 50.0
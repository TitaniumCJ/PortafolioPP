from .espacio import EspacioParqueo, TipoEspacio

class Estacionamiento:
    def __init__(self, politica):
        # lista de lugares iniciales
        self.espacios = [
            EspacioParqueo("A1", TipoEspacio.AUTO),
            EspacioParqueo("A2", TipoEspacio.AUTO),
            EspacioParqueo("M1", TipoEspacio.MOTO),
            EspacioParqueo("G1", TipoEspacio.CUALQUIERA)
        ]
        self.tickets_activos = {}
        self.politica = politica
        self.ganancia_total = 0.0
        self.siguiente_id = 1

    def registrar_entrada(self, vehiculo):
        for lugar in self.espacios:
            # revisa si el lugar es compatible
            if not lugar.ocupado and (lugar.permitido.value == vehiculo.tipo.value or lugar.permitido == TipoEspacio.CUALQUIERA):
                lugar.ocupar(vehiculo)
                from .ticket import Ticket
                nuevo_ticket = Ticket(self.siguiente_id, vehiculo, lugar)
                self.tickets_activos[self.siguiente_id] = nuevo_ticket
                self.siguiente_id += 1
                return nuevo_ticket
        return None

    def registrar_salida(self, id_ticket: int, horas: float):
        # valida que el ticket sea real
        if id_ticket not in self.tickets_activos:
            return None
        
        ticket = self.tickets_activos.pop(id_ticket)
        ticket.espacio.liberar()
        ticket.cerrar()
        
        costo = self.politica.calcular(horas, ticket.vehiculo.tipo.value)
        self.ganancia_total += costo
        return costo
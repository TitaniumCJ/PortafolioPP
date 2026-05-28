---
title: "Práctica 2: Simulador de Estacionamiento"
date: 2026-03-29
draft: false
---

# Reporte de Práctica 02: Simulador de Estacionamiento
[cite_start]**Materia:** Paradigmas de la Programación [cite: 12]
**Profesor:** M.I. [cite_start]José Carlos Gallegos Mariscal [cite: 12]

## 1. Introducción
[cite_start]El problema consiste en administrar un estacionamiento que controla lugares (spots), vehículos y tickets de entrada y salida[cite: 14]. [cite_start]El objetivo es aplicar los pilares de la Programación Orientada a Objetos (POO) para gestionar la ocupación y el cobro mediante un sistema que incluye una interfaz web con Flask[cite: 15].

## 2. Modelo del dominio
[cite_start]El sistema se basa en la interacción de entidades que representan el mundo real del estacionamiento[cite: 17].

### Lista de clases y responsabilidades
* [cite_start]**Vehiculo:** Clase base para representar los autos y motos[cite: 39].
* [cite_start]**Espacio Parqueo:** Controla si un lugar está libre u ocupado y qué tipo de vehículo acepta[cite: 40].
* [cite_start]**Ticket:** Registra los datos de la estancia y el estado de la transacción[cite: 41].
* [cite_start]**Estacionamiento:** Es la clase principal que administra la colección de espacios y tickets[cite: 42].
* [cite_start]**PoliticaTarifa:** Define el contrato para calcular los cobros de forma polimórfica[cite: 43].

## 3. Evidencia de conceptos POO
[cite_start]A continuación se presentan fragmentos de código que demuestran la aplicación del paradigma[cite: 45]:

### Encapsulación
[cite_start]Se protegen los atributos del ticket y se valida que el ID exista antes de procesar una salida en `registrar_salida`[cite: 46].
```python
def registrar_salida(self, id_ticket, horas):
    # Validacion de existencia
    if id_ticket not in self.tickets_activos:
        print("error el id no existe")
        return None
        
    ticket = self.tickets_activos[id_ticket]
    total = self.politica_tarifa.calcular(horas, ticket.vehiculo.tipo)
    ticket.cerrar()
    print("salida procesada correctamente")
    return total
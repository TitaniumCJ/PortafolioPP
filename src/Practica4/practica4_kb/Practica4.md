---
title: "Práctica 4: El Paradigma Lógico con Prolog"
date: 2026-05-27
draft: false
---

# Reporte de Práctica: El Paradigma Lógico con Prolog

## Sesión 1: Introducción a Prolog
Se configuró el entorno y se analizaron las estructuras sintácticas básicas del lenguaje.
* **Hechos:** Declaraciones absolutas sobre el dominio, como `cat(tom).` o `lazy(juan).` Todos empiezan con minúscula y deben terminar obligatoriamente con un punto.
* **Reglas:** Cláusulas condicionales que definen una relación si se cumplen las condiciones del cuerpo mediante el operador `:-` Por ejemplo: `happy(lili) :- dances(lili).`
* **Consultas:** Preguntas realizadas para verificar la veracidad de una relación dentro de la base de conocimientos.

## Sesión 2: Relaciones Complejas y Listas
Se expandieron las bases de conocimiento y se trabajó con operaciones avanzadas.
* **Relaciones Familiares:** En archivos como `family_ext.pl` se implementaron reglas para determinar parentescos como `sister/2` y `brother/2` Se incluyó la restricción de desigualdad `X \== Y` para evitar que una persona sea su propio hermano. También se analizó la recursión mediante la regla `predecessor/2` para rastrear ancestros entre generaciones.
* **Listas:** Se representaron con la sintaxis `[Head|Tail]` para separar el primer elemento (cabecera) del resto (cola). Se utilizaron operaciones para verificar membresía, calcular longitud y concatenar elementos.

## Sesión 3: Aplicaciones Prácticas
Se añadieron soluciones declarativas para los problemas lógicos planteados.
* **Torres de Hanoi:** Se implementó una resolución recursiva para calcular la secuencia exacta de movimientos necesarios para trasladar los discos entre los postes.
* **El Mono y el Plátano:** Se modeló un espacio de estados definiendo la situación del mono y la caja (`en_suelo`, `en_caja`) junto con las transiciones válidas (`caminar`, `empujar`, `subir`, `tomar`) para alcanzar el objetivo.
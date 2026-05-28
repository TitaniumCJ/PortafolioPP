#include <stdio.h>
#include <stdlib.h>
#include "cola.h"

Job_t* frente = NULL; // Inicio de cola
Job_t* final = NULL;  // Fin de cola

void enqueue() {
    Job_t* nuevo = (Job_t*)malloc(sizeof(Job_t)); // Reserva memoria heap
    if (!nuevo) return;
    
    printf("Usuario: ");
    scanf("%s", nuevo->user);
    printf("Paginas: ");
    scanf("%d", &nuevo->pags);
    nuevo->id = rand() % 1000;
    nuevo->next = NULL;

    if (frente == NULL) {
        frente = final = nuevo;
    } else {
        final->next = nuevo;
        final = nuevo; // Actualiza final
    }
}

void peek() {
    if (frente == NULL) return;
    printf("Siguiente: %s\n", frente->user);
}

void dequeue() {
    if (frente == NULL) return;
    Job_t* temp = frente;
    frente = frente->next; // Mueve frente
    if (frente == NULL) final = NULL;
    free(temp); // Libera memoria
}

void listar() {
    Job_t* temp = frente;
    while (temp != NULL) { // Recorre nodos
        printf("[%d] %s\n", temp->id, temp->user);
        temp = temp->next;
    }
}

void simular() {
    while (frente != NULL) {
        printf("Procesando... %s\n", frente->user);
        dequeue();
    }
}
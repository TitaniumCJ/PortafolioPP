#ifndef COLA_H
#define COLA_H

// Estructura del trabajo
typedef struct Job {
    int id;
    char user[30];
    int pags;
    struct Job* next;
} Job_t;

// Prototipos de funciones
void enqueue();
void peek();
void dequeue();
void listar();
void simular();

#endif
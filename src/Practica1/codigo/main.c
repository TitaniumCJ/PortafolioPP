#include <stdio.h>
#include "cola.h" // Conecta con la logica

int main() {
    int op;
    do {
        printf("\n1. Agregar\n2. Ver Siguiente\n3. Listar\n4. Simular\n5. Salir\nOpcion: ");
        scanf("%d", &op);
        
        switch(op) {
            case 1: enqueue(); break;
            case 2: peek(); break;
            case 3: listar(); break;
            case 4: simular(); break;
        }
    } while (op != 5); // Control de secuencia
    
    return 0;
}
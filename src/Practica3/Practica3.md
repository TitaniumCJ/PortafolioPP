## **Reporte de Practica: Entorno Haskell y Aplicacion TODO**

### **1\. Datos Generales**

* **Nombre:** Carlos Alberto Jaime Mascareño  
* **Matricula:** 377175  
* **Institución:** Universidad Autonoma de Baja California  
* **Materia:** Paradigmas de Programación

### **2\. Instalación del Entorno (Sesion 1\)**

Para esta sesión se configuró el ecosistema de desarrollo utilizando la herramienta **GHCup** para Windows. Los componentes instalados y verificados son:

* **GHC (Glasgow Haskell Compiler) 9.6.7:** El compilador encargado de transformar el codigo fuente en archivos ejecutables.  
* **Stack 3.7.1:** Herramienta para la gestion de proyectos y dependencias, asegurando que la aplicacion sea reproducible.  
* **Cabal:** Sistema de infraestructura para la construccion de paquetes en Haskell.  
* **HLS (Haskell Language Server):** Motor que proporciona ayuda en tiempo real, autocompletado y deteccion de errores en el editor de codigo.

### **3\. Comparativa: Paradigma Imperativo (C) vs. Funcional (Haskell)**

Basado en la guia de Chalmers y la experiencia previa en C:

* **Control de Flujo:** Mientras que en C se utilizan ciclos `for` o `while`, en Haskell se utiliza la **recursividad** para procesar listas de tareas.  
* **Estado y Datos:** En C las variables cambian su valor (mutabilidad). En Haskell los datos son **inmutables**, lo que significa que al "modificar" una lista de tareas, en realidad se genera una nueva version de la misma.  
* **Pureza:** Haskell separa las funciones puras (calculos) de las impuras (entrada/salida) mediante el uso de **Monadas**, garantizando un codigo mas predecible.

### **4\. Analisis de la Aplicacion TODO (Sesion 2\)**

La aplicacion desarrollada permite gestionar una lista de actividades de forma interactiva. Su funcionamiento se describe a continuacion:

* **Estructura del Proyecto:** Utiliza la arquitectura de **Stack**, donde el codigo principal reside en `app/Main.hs` y la configuracion de dependencias en `package.yaml`.  
* **Gestion de la Lista:** Las tareas se almacenan en una estructura de datos de tipo lista de cadenas (`[String]`).  
* **Ciclo de Ejecucion:** La aplicacion emplea una funcion recursiva para mantener el menu activo. Al seleccionar una opcion, se pasa la lista de tareas actualizada a la siguiente iteracion.  
* **Interactividad:** Se utiliza el **IO Monad** para permitir que el programa lea instrucciones del usuario y muestre resultados en la terminal de Windows.


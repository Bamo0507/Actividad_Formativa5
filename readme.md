# Actividad Formativa 5 Matemática Dicreta (Algoritmos en Python)

## **Descripción**

Este proyecto es una colección de algoritmos matemáticos implementados en Python que incluyen:

- **Criba de Eratóstenes**: Para generar números primos hasta un límite dado.
- **Verificación de Primalidad**: Para verificar si un número es primo.
- **Algoritmo Euclidiano**: Para calcular el Máximo Común Divisor (MCD) de dos números.
- **Coeficientes de Bézout**: Para encontrar los coeficientes que satisfacen la ecuación de Bézout para dos números dados.

El programa principal presenta un menú interactivo que permite al usuario seleccionar y ejecutar cualquiera de estos algoritmos, facilitando una experiencia de uso sencilla y eficiente.

## **Estructura del Proyecto**

project/
│ ├── lib/
│ ├── utils.py
│ └── bezout.py
├── criba.py
├── euclidean.py
├── isPrime.py
├── main.py
│ ├── tests/
│ ├── test_utils.py
│ ├── test_euclidean.py
│ ├── test_bezout.py
│ ├── test_criba.py
│ ├── test_isPrime.py
│ └── README.md

- **lib/utils.py**: Contiene funciones de validación utilizadas por otros módulos.
- **bezout.py**: Implementa el algoritmo de Bézout para encontrar coeficientes que satisfacen la ecuación de Bézout.
- **criba.py**: Implementa la Criba de Eratóstenes para generar números primos hasta un límite dado.
- **euclidean.py**: Implementa el Algoritmo Euclidiano para calcular el MCD de dos números.
- **isPrime.py**: Implementa una función para verificar si un número es primo.
- **main.py**: Programa principal que presenta un menú interactivo para ejecutar los diferentes algoritmos.
- **tests/**: Carpeta que contiene pruebas unitarias para cada módulo.
- **README.md**: Este archivo, que proporciona una descripción completa del proyecto.

## **Instalación de Prerequisitos**

Antes de ejecutar el programa, asegúrate de tener instalado Python 3.x en tu sistema. Además, el proyecto requiere la biblioteca `numpy` para operaciones matriciales.

### **1. Instalar Python**

Descarga e instala Python desde la [página oficial de Python](https://www.python.org/downloads/) si aún no lo tienes instalado.

### **2. Clonar el Repositorio**

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Bamo0507/Actividad_Formativa5.git
cd Actividad_Formativa5
```

## 1. Instalar Dependencias

Instala la biblioteca numpy utilizando pip:

```bash
pip install numpy
```

## 2. (Opcional) Ejecutar Pruebas Unitarias

Para asegurarte de que todo está funcionando correctamente, puedes ejecutar las pruebas unitarias:

```bash
python -m unittest discover -s tests
```

## 3. Funcionamiento del Programa

1. Ejecutar el Programa Principal
   Para iniciar el programa, ejecuta el archivo main.py:

```bash
python main.py
```

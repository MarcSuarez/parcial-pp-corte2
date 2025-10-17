# 🧠 Parcial — Corte 2

Este repositorio contiene los **tres puntos del parcial** desarrollados en **Python** y **Kotlin**, aplicando conceptos de **Programación Orientada a Objetos (POO)** y **Sistemas Multiagentes**.

---

## 📁 Estructura del Proyecto

```
parcial/
│
├── punto 1/   → Perceptrón basado en agentes (Python + Mesa)
├── punto 2/   → Calculadora simple basada en agentes (Python + Mesa)
└── punto 3/   → Calculadora científica con POO (Kotlin)
```

---

## ⚙️ Requisitos Generales

### 🐍 Para los puntos 1 y 2
- Python 3.10 o superior
- Librerías indicadas en `requirements.txt`
- (Opcional) Entorno virtual recomendado con Anaconda o venv

Instalar dependencias con:
```bash
pip install -r requirements.txt
```

### ☕ Para el punto 3
- Kotlin instalado en el sistema  
  Verifica la instalación con:
  ```bash
  kotlin -version
  ```
- Java JDK 8 o superior  
  Verifica con:
  ```bash
  java -version
  ```

---

## 🧩 Punto 1 — Perceptrón basado en Agentes

### 📘 Descripción
Simulación de un **modelo Perceptrón** utilizando la librería **Mesa (Python)**.  
Cada agente representa una neurona que aprende mediante ajustes de pesos, visualizando su aprendizaje en una interfaz web.

### ▶️ Ejecución

1. Entra a la carpeta del punto 1:
   ```bash
   cd "punto 1"
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el programa:
   ```bash
   python run.py
   ```

4. Abre en tu navegador la URL que aparecerá (por defecto `http://127.0.0.1:8521/`).

---

## 🧮 Punto 2 — Calculadora basada en Agentes

### 📘 Descripción
Una **calculadora simple** desarrollada también con **Mesa (Python)**, donde cada agente representa una operación matemática (suma, resta, multiplicación, división).  
El modelo permite observar cómo los agentes cooperan para resolver cálculos distribuidos.

### ▶️ Ejecución

1. Entra a la carpeta del punto 2:
   ```bash
   cd "punto 2"
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el programa:
   ```bash
   python main.py
   ```

4. Abre la interfaz web en el enlace que indique la consola (por defecto `http://127.0.0.1:8521/`).

---

## 🧠 Punto 3 — Calculadora Científica con POO

### 📘 Descripción
Implementación de una **calculadora científica en Kotlin**, aplicando los principios de la **Programación Orientada a Objetos (POO)**:  
**encapsulamiento**, **herencia** y **polimorfismo**.

### ▶️ Ejecución

1. Entra a la carpeta del punto 3:
   ```bash
   cd "punto 3"
   ```

2. Compila el proyecto:
   ```bash
   kotlinc *.kt -include-runtime -d calculadora.jar
   ```

3. Ejecuta el programa:
   ```bash
   java -jar calculadora.jar
   ```

### 💡 Nota
Asegúrate de tener instalado Kotlin y Java.  
Si ves el error `no main manifest attribute, in calculadora.jar`, revisa que tu `Main.kt` contenga una función `fun main()` válida.

---

## 📄 Autor

**Marc Suárez Molina**  
Proyecto académico — Programación Orientada a Objetos (POO)  
Universidad / Curso: *Parcial — Segundo Corte*

# Calculadora Científica en Kotlin 🧮

Este proyecto implementa una **Calculadora Científica** en **Kotlin**, aplicando los principios de la **Programación Orientada a Objetos (POO)**: **encapsulamiento**, **herencia** y **polimorfismo**.

---

## 🚀 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- [Kotlin](https://kotlinlang.org/docs/command-line.html)
- [Java JDK 8 o superior](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- Sistema operativo compatible: **Linux**, **Windows** o **macOS**

Verifica que Kotlin esté correctamente instalado ejecutando:

```bash
kotlin -version
```

Y para verificar Java:

```bash
java -version
```

---

## 📂 Estructura del Proyecto

```
parcial/
│
├── Calculadora.kt
├── CalculadoraCientifica.kt
├── Memoria.kt
├── EvaluadorExpresiones.kt
├── Main.kt
└── README.md
```

---

## ⚙️ Cómo Compilar y Ejecutar

### 1️⃣ Compilar todos los archivos Kotlin

Desde la terminal, entra a la carpeta del proyecto y ejecuta:

```bash
kotlinc *.kt -include-runtime -d main.jar
```

Esto generará un archivo `main.jar` que contiene todo el proyecto compilado.

### 2️⃣ Ejecutar el programa

```bash
java -jar main.jar
```

> 💡 Si obtienes el error:  
> `no main manifest attribute, in main.jar`  
> asegúrate de que tu archivo `Main.kt` contenga una función `fun main()` y que esté bien escrita.

---

## 🧠 Principios POO aplicados

- **Encapsulamiento:**  
  Cada clase tiene sus propios atributos y métodos. Por ejemplo, la memoria de la calculadora está protegida dentro de `CalculadoraCientifica` y solo puede modificarse mediante métodos públicos.

- **Herencia:**  
  La clase `CalculadoraCientifica` **hereda** de `Calculadora`, reutilizando las operaciones básicas y extendiendo las funcionalidades con métodos científicos.

- **Polimorfismo:**  
  Se aplican sobrecargas de métodos (por ejemplo, `sumar()` y `restar()` para enteros y decimales). Esto permite usar el mismo nombre de método con diferentes tipos de datos.

---

## 🧾 Menú del Programa

El programa principal (`Main.kt`) muestra un menú interactivo con opciones:

| Opción | Descripción |
|:------:|--------------|
| 1 | Suma |
| 2 | Resta |
| 3 | Multiplicación |
| 4 | División |
| 5 | Seno |
| 6 | Coseno |
| 7 | Tangente |
| 8 | Potencia |
| 9 | Raíz cuadrada |
| 10 | Logaritmos y exponenciales |
| 11 | Operaciones con memoria |
| 12 | Evaluar expresión completa |
| 0 | Salir del programa |

---

## 🧪 Ejemplo de Uso

```bash
$ java -jar main.jar

==== CALCULADORA CIENTÍFICA ====
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Seno
6. Coseno
...
Seleccione una opción: 1
Ingrese el primer número: 5
Ingrese el segundo número: 3
Resultado: 8.0
```

---

## 🧰 Autor

**Marc Suárez Molina**  
Proyecto académico — Programación Orientada a Objetos (POO)  
Universidad / Curso: *Parcial — Segundo Corte*

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**, por lo que puede ser usado y modificado libremente con fines educativos.

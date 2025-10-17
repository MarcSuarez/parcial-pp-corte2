import kotlin.math.*

/**
 * Clase base Calculadora con operaciones básicas
 */
open class Calculadora {
    
    /**
     * Realiza la suma de dos números
     */
    open fun sumar(a: Double, b: Double): Double = a + b
    
    /**
     * Realiza la resta de dos números
     */
    open fun restar(a: Double, b: Double): Double = a - b
    
    /**
     * Realiza la multiplicación de dos números
     */
    open fun multiplicar(a: Double, b: Double): Double = a * b
    
    /**
     * Realiza la división de dos números
     * @throws ArithmeticException si el divisor es cero
     */
    open fun dividir(a: Double, b: Double): Double {
        if (b == 0.0) {
            throw ArithmeticException("Error: División por cero no permitida")
        }
        return a / b
    }
    
    // Sobrecarga para operaciones con enteros
    fun sumar(a: Int, b: Int): Int = a + b
    fun restar(a: Int, b: Int): Int = a - b
    fun multiplicar(a: Int, b: Int): Int = a * b
    fun dividir(a: Int, b: Int): Int {
        if (b == 0) {
            throw ArithmeticException("Error: División por cero no permitida")
        }
        return a / b
    }
}

/**
 * Clase derivada CalculadoraCientifica con operaciones avanzadas
 */
class CalculadoraCientifica : Calculadora() {
    
    private var memoria: Double = 0.0
    
    // ==================== FUNCIONES TRIGONOMÉTRICAS ====================
    
    /**
     * Calcula el seno de un ángulo en grados
     */
    fun seno(angulo: Double): Double = sin(Math.toRadians(angulo))
    
    /**
     * Calcula el coseno de un ángulo en grados
     */
    fun coseno(angulo: Double): Double = cos(Math.toRadians(angulo))
    
    /**
     * Calcula la tangente de un ángulo en grados
     * @throws ArithmeticException si el ángulo es múltiplo impar de 90
     */
    fun tangente(angulo: Double): Double {
        val anguloNormalizado = angulo % 180
        if (abs(anguloNormalizado - 90) < 1e-10) {
            throw ArithmeticException("Error: La tangente de 90° no está definida")
        }
        return tan(Math.toRadians(angulo))
    }
    
    // ==================== POTENCIAS Y RAÍCES ====================
    
    /**
     * Calcula la potencia de un número
     */
    fun potencia(base: Double, exponente: Double): Double = base.pow(exponente)
    
    /**
     * Calcula la raíz cuadrada de un número
     * @throws ArithmeticException si el número es negativo
     */
    fun raizCuadrada(numero: Double): Double {
        if (numero < 0) {
            throw ArithmeticException("Error: No se puede calcular la raíz cuadrada de un número negativo")
        }
        return sqrt(numero)
    }
    
    /**
     * Calcula la raíz n-ésima de un número
     */
    fun raizN(numero: Double, n: Double): Double {
        if (numero < 0 && n % 2 == 0.0) {
            throw ArithmeticException("Error: No se puede calcular raíz par de un número negativo")
        }
        return numero.pow(1.0 / n)
    }
    
    // ==================== LOGARITMOS ====================
    
    /**
     * Calcula el logaritmo en base 10
     * @throws ArithmeticException si el número es menor o igual a cero
     */
    fun logaritmoBase10(numero: Double): Double {
        if (numero <= 0) {
            throw ArithmeticException("Error: El logaritmo de números menores o iguales a cero no está definido")
        }
        return log10(numero)
    }
    
    /**
     * Calcula el logaritmo natural (base e)
     * @throws ArithmeticException si el número es menor o igual a cero
     */
    fun logaritmoNatural(numero: Double): Double {
        if (numero <= 0) {
            throw ArithmeticException("Error: El logaritmo de números menores o iguales a cero no está definido")
        }
        return ln(numero)
    }
    
    // ==================== FUNCIONES EXPONENCIALES ====================
    
    /**
     * Calcula e elevado a la potencia x
     */
    fun exponencial(x: Double): Double = exp(x)
    
    // ==================== CONVERSIÓN DE ÁNGULOS ====================
    
    /**
     * Convierte grados a radianes
     */
    fun gradosARadianes(grados: Double): Double = Math.toRadians(grados)
    
    /**
     * Convierte radianes a grados
     */
    fun radianesAGrados(radianes: Double): Double = Math.toDegrees(radianes)
    
    // ==================== FUNCIONES DE MEMORIA ====================
    
    /**
     * Suma un valor a la memoria (M+)
     */
    fun memoriaAgregar(valor: Double) {
        memoria += valor
        println("Memoria: $memoria")
    }
    
    /**
     * Resta un valor de la memoria (M-)
     */
    fun memoriaRestar(valor: Double) {
        memoria -= valor
        println("Memoria: $memoria")
    }
    
    /**
     * Recupera el valor de la memoria (MR)
     */
    fun memoriaRecuperar(): Double {
        println("Recuperando de memoria: $memoria")
        return memoria
    }
    
    /**
     * Limpia la memoria (MC)
     */
    fun memoriaLimpiar() {
        memoria = 0.0
        println("Memoria limpiada")
    }
    
    // ==================== EVALUACIÓN DE EXPRESIONES ====================
    
    /**
     * Evalúa una expresión matemática completa
     * Soporta operaciones básicas y funciones científicas
     */
    fun evaluarExpresion(expresion: String): Double {
        try {
            val expresionLimpia = expresion.replace(" ", "").lowercase()
            return evaluarExpresionRecursiva(expresionLimpia)
        } catch (e: Exception) {
            throw ArithmeticException("Error al evaluar la expresión: ${e.message}")
        }
    }
    
    private fun evaluarExpresionRecursiva(expr: String): Double {
        // Procesar funciones científicas primero
        var expresion = procesarFunciones(expr)
        
        // Evaluar suma y resta (menor precedencia)
        var i = expresion.length - 1
        var parentesisCount = 0
        while (i >= 0) {
            when (expresion[i]) {
                ')' -> parentesisCount++
                '(' -> parentesisCount--
                '+', '-' -> {
                    if (parentesisCount == 0 && i > 0) {
                        val izq = expresion.substring(0, i)
                        val der = expresion.substring(i + 1)
                        return if (expresion[i] == '+') {
                            evaluarExpresionRecursiva(izq) + evaluarExpresionRecursiva(der)
                        } else {
                            evaluarExpresionRecursiva(izq) - evaluarExpresionRecursiva(der)
                        }
                    }
                }
            }
            i--
        }
        
        // Evaluar multiplicación y división
        i = expresion.length - 1
        parentesisCount = 0
        while (i >= 0) {
            when (expresion[i]) {
                ')' -> parentesisCount++
                '(' -> parentesisCount--
                '*', '/' -> {
                    if (parentesisCount == 0) {
                        val izq = expresion.substring(0, i)
                        val der = expresion.substring(i + 1)
                        return if (expresion[i] == '*') {
                            evaluarExpresionRecursiva(izq) * evaluarExpresionRecursiva(der)
                        } else {
                            dividir(evaluarExpresionRecursiva(izq), evaluarExpresionRecursiva(der))
                        }
                    }
                }
            }
            i--
        }
        
        // Evaluar potencias
        i = expresion.length - 1
        parentesisCount = 0
        while (i >= 0) {
            when (expresion[i]) {
                ')' -> parentesisCount++
                '(' -> parentesisCount--
                '^' -> {
                    if (parentesisCount == 0) {
                        val izq = expresion.substring(0, i)
                        val der = expresion.substring(i + 1)
                        return potencia(evaluarExpresionRecursiva(izq), evaluarExpresionRecursiva(der))
                    }
                }
            }
            i--
        }
        
        // Remover paréntesis externos
        if (expresion.startsWith("(") && expresion.endsWith(")")) {
            return evaluarExpresionRecursiva(expresion.substring(1, expresion.length - 1))
        }
        
        // Número simple
        return expresion.toDoubleOrNull() ?: throw NumberFormatException("Expresión inválida: $expresion")
    }
    
    private fun procesarFunciones(expr: String): String {
        var resultado = expr
        
        // Procesar sin, cos, tan, log, ln, sqrt, exp
        val funciones = listOf("sin", "cos", "tan", "log", "sqrt", "exp")
        
        for (funcion in funciones) {
            while (resultado.contains(funcion)) {
                val inicio = resultado.indexOf(funcion)
                val parentesisInicio = inicio + funcion.length
                
                if (parentesisInicio < resultado.length && resultado[parentesisInicio] == '(') {
                    var parentesisCount = 1
                    var i = parentesisInicio + 1
                    
                    while (i < resultado.length && parentesisCount > 0) {
                        when (resultado[i]) {
                            '(' -> parentesisCount++
                            ')' -> parentesisCount--
                        }
                        i++
                    }
                    
                    val argumento = resultado.substring(parentesisInicio + 1, i - 1)
                    val valorArgumento = evaluarExpresionRecursiva(argumento)
                    
                    val valorFuncion = when (funcion) {
                        "sin" -> seno(valorArgumento)
                        "cos" -> coseno(valorArgumento)
                        "tan" -> tangente(valorArgumento)
                        "log" -> logaritmoBase10(valorArgumento)
                        "ln" -> logaritmoNatural(valorArgumento)
                        "sqrt" -> raizCuadrada(valorArgumento)
                        "exp" -> exponencial(valorArgumento)
                        else -> valorArgumento
                    }
                    
                    resultado = resultado.substring(0, inicio) + valorFuncion.toString() + resultado.substring(i)
                } else {
                    break
                }
            }
        }
        
        return resultado
    }
}

/**
 * Clase principal para la interfaz de usuario
 */
class InterfazCalculadora(private val calculadora: CalculadoraCientifica) {
    
    fun mostrarMenu() {
        println("\n╔════════════════════════════════════════════╗")
        println("║    CALCULADORA CIENTÍFICA EN KOTLIN        ║")
        println("╚════════════════════════════════════════════╝")
        println("\n--- OPERACIONES BÁSICAS ---")
        println("1. Suma")
        println("2. Resta")
        println("3. Multiplicación")
        println("4. División")
        println("\n--- OPERACIONES CIENTÍFICAS ---")
        println("5. Seno")
        println("6. Coseno")
        println("7. Tangente")
        println("8. Potencia")
        println("9. Raíz Cuadrada")
        println("10. Raíz N-ésima")
        println("11. Logaritmo Base 10")
        println("12. Logaritmo Natural")
        println("13. Exponencial (e^x)")
        println("\n--- CONVERSIONES ---")
        println("14. Grados a Radianes")
        println("15. Radianes a Grados")
        println("\n--- MEMORIA ---")
        println("16. M+ (Agregar a memoria)")
        println("17. M- (Restar de memoria)")
        println("18. MR (Recuperar memoria)")
        println("19. MC (Limpiar memoria)")
        println("\n--- AVANZADO ---")
        println("20. Evaluar Expresión")
        println("0. Salir")
        print("\nSeleccione una opción: ")
    }
    
    fun ejecutar() {
        while (true) {
            try {
                mostrarMenu()
                val opcion = readLine()?.toIntOrNull() ?: continue
                
                when (opcion) {
                    0 -> {
                        println("\n¡Gracias por usar la Calculadora Científica!")
                        break
                    }
                    1 -> operacionDoble("Suma") { a, b -> calculadora.sumar(a, b) }
                    2 -> operacionDoble("Resta") { a, b -> calculadora.restar(a, b) }
                    3 -> operacionDoble("Multiplicación") { a, b -> calculadora.multiplicar(a, b) }
                    4 -> operacionDoble("División") { a, b -> calculadora.dividir(a, b) }
                    5 -> operacionSimple("Seno (grados)") { calculadora.seno(it) }
                    6 -> operacionSimple("Coseno (grados)") { calculadora.coseno(it) }
                    7 -> operacionSimple("Tangente (grados)") { calculadora.tangente(it) }
                    8 -> operacionDoble("Potencia") { a, b -> calculadora.potencia(a, b) }
                    9 -> operacionSimple("Raíz Cuadrada") { calculadora.raizCuadrada(it) }
                    10 -> operacionDoble("Raíz N-ésima") { a, b -> calculadora.raizN(a, b) }
                    11 -> operacionSimple("Logaritmo Base 10") { calculadora.logaritmoBase10(it) }
                    12 -> operacionSimple("Logaritmo Natural") { calculadora.logaritmoNatural(it) }
                    13 -> operacionSimple("Exponencial") { calculadora.exponencial(it) }
                    14 -> operacionSimple("Grados a Radianes") { calculadora.gradosARadianes(it) }
                    15 -> operacionSimple("Radianes a Grados") { calculadora.radianesAGrados(it) }
                    16 -> {
                        print("Ingrese el valor a agregar a memoria: ")
                        val valor = leerDouble()
                        calculadora.memoriaAgregar(valor)
                    }
                    17 -> {
                        print("Ingrese el valor a restar de memoria: ")
                        val valor = leerDouble()
                        calculadora.memoriaRestar(valor)
                    }
                    18 -> {
                        val valor = calculadora.memoriaRecuperar()
                        println("Valor en memoria: $valor")
                    }
                    19 -> calculadora.memoriaLimpiar()
                    20 -> {
                        println("\nEjemplos: 2+3*4, sin(45)+cos(30), 2^3+log(100)")
                        print("Ingrese la expresión: ")
                        val expresion = readLine() ?: ""
                        val resultado = calculadora.evaluarExpresion(expresion)
                        println("Resultado: $resultado")
                    }
                    else -> println("⚠ Opción no válida")
                }
                
                if (opcion != 0) {
                    print("\nPresione Enter para continuar...")
                    readLine()
                }
                
            } catch (e: ArithmeticException) {
                println("\n⚠ ${e.message}")
                print("Presione Enter para continuar...")
                readLine()
            } catch (e: Exception) {
                println("\n⚠ Error: ${e.message}")
                print("Presione Enter para continuar...")
                readLine()
            }
        }
    }
    
    private fun operacionSimple(nombre: String, operacion: (Double) -> Double) {
        print("\nIngrese el valor: ")
        val valor = leerDouble()
        val resultado = operacion(valor)
        println("$nombre de $valor = $resultado")
    }
    
    private fun operacionDoble(nombre: String, operacion: (Double, Double) -> Double) {
        print("\nIngrese el primer valor: ")
        val a = leerDouble()
        print("Ingrese el segundo valor: ")
        val b = leerDouble()
        val resultado = operacion(a, b)
        println("$nombre: $a y $b = $resultado")
    }
    
    private fun leerDouble(): Double {
        while (true) {
            try {
                return readLine()?.toDouble() ?: throw NumberFormatException()
            } catch (e: NumberFormatException) {
                print("⚠ Entrada inválida. Ingrese un número válido: ")
            }
        }
    }
}

/**
 * Función principal
 */
fun main() {
    val calculadoraCientifica = CalculadoraCientifica()
    val interfaz = InterfazCalculadora(calculadoraCientifica)
    interfaz.ejecutar()
}
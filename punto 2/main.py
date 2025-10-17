from calculator_model import CalculatorModel


def run_tests(calculator):
    """Ejecuta pruebas automáticas"""
    test_cases = [
        "2 + 3",
        "10 - 5",
        "4 * 5",
        "20 / 4",
        "2 ^ 3",
        "2 + 3 * 4",
        "2 + 3 * 4 - 5",
        "(2 + 3) * 4",
        "10 / 2 + 3 * 4",
        "2 ^ 3 + 4 * 5 - 6 / 2",
        "3.5 + 2.5 * 4",
        "100 / 4 / 5",
        "2 ^ 2 ^ 3"
    ]
    
    print("\n--- PRUEBAS AUTOMÁTICAS ---\n")
    for expression in test_cases:
        try:
            result = calculator.calculate(expression)
            print(f"Expresión: {expression:30s} | Resultado: {result}")
        except Exception as e:
            print(f"Expresión: {expression:30s} | Error: {e}")


def interactive_mode(calculator):
    """Modo interactivo de la calculadora"""
    print("\n" + "=" * 60)
    print("\n--- MODO INTERACTIVO ---")
    print("Escribe 'salir' para terminar\n")
    
    while True:
        expression = input("\nIngresa una expresión: ").strip()
        
        if expression.lower() in ['salir', 'exit', 'quit']:
            print("\n¡Hasta luego!")
            break
            
        if not expression:
            continue
            
        try:
            result = calculator.calculate(expression)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Función principal"""
    print("=" * 60)
    print("CALCULADORA BASADA EN AGENTES (MESA)")
    print("=" * 60)
    print("\nOperaciones soportadas: +, -, *, /, ^ (potencia)")
    print("Ejemplo: 2 + 3 * 4 - 5")
    print("=" * 60)
    
    # Crear la calculadora
    calculator = CalculatorModel()
    
    # Ejecutar pruebas
    run_tests(calculator)
    
    # Modo interactivo
    interactive_mode(calculator)


if __name__ == "__main__":
    main()
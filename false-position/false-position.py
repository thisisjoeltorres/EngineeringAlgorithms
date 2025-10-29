import math

# Request the details of the function and the interva;.

print("Bienvenido a la calculadora de Falsa Posicion. Por favor, ingrese los detalles de su funcion e intervalos correspondientes.")

intervalStart = float(input("Inicio de su intervalo (a): "))
intervalEnd = float(input("Final de su intervalo (b): "))
maxError = float(input("Ingrese el valor maximo de error en decimales (e): "))

# Funcion

def user_function(x):
  functionResult = (math.e**(3*x)) - 4

  result = round(functionResult, 4) # Aca ira la funcion del usuario
  return result

def false_position(a, b):
    return (a * user_function(b) - b * user_function(a)) / (user_function(b) - user_function(a))

# Falsa Posicion

interA = intervalStart
interB = intervalEnd
solution = 0
currentError = 1
iterationCounter = 0
previousFalse = 0

while (currentError > maxError):
    # Calculamos f(a), f(b), f(xi)

    funcA = user_function(interA)
    funcB = user_function(interB)
    funcXi = false_position(interA, interB)

    # Determinar nuevo intervalo.

    if ((funcA * funcXi) < 0):
        interB = funcXi
    else:
        interA = funcXi

    # Determinar valor de error y comprobar

    if (iterationCounter > 0):
        currentError = abs(funcXi - solution)
    solution = funcXi
    iterationCounter = iterationCounter + 1

    # Imprimir resultados iteracion.

    print(f"\n------- Interacion Actual: {iterationCounter} ----------")
    print(f"Error actual: {currentError}")
    print(f"Nuevo intervalo: a = {interA}, b = {interB}")
    print(f"La solucion hasta aca es: {solution}")
    print(f"f(a) = {funcA}, f(b) = {funcB}, f(xi) = {funcXi}")

print(f"\nLA RAIZ FINAL ES: {solution}\n")
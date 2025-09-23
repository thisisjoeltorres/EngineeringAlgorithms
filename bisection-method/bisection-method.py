import math

# Request the details of the function and the interva;.

print("Bienvenido a la calculadora de Biseccion. Por favor, ingrese los detalles de su funcion e intervalos correspondientes.")

intervalStart = float(input("Inicio de su intervalo (a): "))
intervalEnd = float(input("Final de su intervalo (b): "))
maxError = float(input("Ingrese el valor maximo de error en decimales (e): "))

# Funcion

def user_function(x):
  if x == 0:
    return "Error: x no puede ser cero."
    
  # Calcular cada parte de la expresion por separado.

  term1 = math.cos(2/x)
  term2 = 2 * math.sin(1/x)
  term3 = 1/x
    
  # Combinar y redondear a 4 espacios decimales.

  result = round(term1 - term2 + term3, 4)
  return result

# Biseccion

interA = intervalStart
interB = intervalEnd
solution = 0
currentError = 1
iterationCounter = 0

while (currentError > maxError):

    # Dividimos intervalo por la mitad.
    
    c = (interA + interB) / 2

    # Calculamos f(a), f(b), f(m)

    funcA = user_function(interA)
    funcB = user_function(interB)
    funcM = user_function(c)

    # Determinar nuevo intervalo.

    if ((funcA * funcM) < 0):
        interB = c
    else:
        interA = c

    # Determinar valor de error y comprobar

    currentError = (interB - interA) / 2
    solution = c
    iterationCounter = iterationCounter + 1

    # Imprimir resultados iteracion.

    print(f"\n------- Interacion Actual: {iterationCounter} ----------")
    print(f"Error actual: {currentError}")
    print(f"Nuevo intervalo: a = {interA}, b = {interB}")
    print(f"La solucion hasta aca es: {c}")

print(f"\nLA RAIZ FINAL ES: {c}\n")
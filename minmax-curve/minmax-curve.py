# 1) Preguntar numero de datos a ingresar (nota, los datos deben ser simetricos). 
# 2) Tomar datos tanto en x como en y. 
# 3) Sacar los valores de (x*y) y (x^2) para cada fila de la tabla. 
# 4) Hacer las sumatorias para x, y, (x*y), (x^2). 
# 5) Aplicar la formula para hallar m. 
# 6) Aplicar la formula para hallar b. 
# 7) Imprimir la recta final (y=mx+b), 
# 8) Graficar.

import math

# Listas donde guardaremos las coordenadas de cada punto.

coordinatesInX = []
coordinatesInY = []
resultsXTimesY = []
resultsXSquared = []

# Definir los puntos iniciales tanto para x como para y.

print("Bienvenido a MinMaxCurve! " \
"El siguiente programa tiene el proposito de buscar la recta que mejor se ajusta a un conjunto de puntos.\n" \
"Primero, definamos la cantidad de datos con los que cuenta la grafica actual.\n")

dotAmmount = int(input("Ingrese la cantidad de puntos presentes en su grafica: ")) # n

# Usamos un ciclo for para tomar cada una de las cordenadas de cada punto.

for dot in range(0, dotAmmount):
    print(f"\n*** Estamos en el punto numero: {dot + 1}.***")
    currentX = int(input("Coordenada en X: "))
    currentY = int(input("Coordenada en Y: "))\
    
    # Guardamos los valores para X y Y.

    coordinatesInX.append(currentX)
    coordinatesInY.append(currentY)

    # Calculamos x*y y x^2 de una vez.

    timesXY = currentX * currentY
    squaredX = currentX ** 2

    # Guardamos en sus respectivas listas.

    resultsXTimesY.append(timesXY)
    resultsXSquared.append(squaredX)

# Almacenamos la sumatoria de cada lista.

sumX = sum(coordinatesInX)
sumY = sum(coordinatesInY)
sumXTimesY = sum(resultsXTimesY)
sumXSquared = sum(resultsXSquared)

# Hallamos m con la formula.

m = (sumXTimesY - ((sumX * sumY) / dotAmmount)) / (sumXSquared - (pow(sumX, 2) / dotAmmount))

# Hallamos b con la formula.

b = (sumY / dotAmmount) - (m * (sumX / dotAmmount))

# Imprimimos los valores.

print(f"\n******* Resultado *******\nLa recta que mejor se ajusta es la siguiente:\n" \
f"Y = {m}x + {b}.\n" \
f"m = {m}\n" \
f"b = {b}\n")

print(f"\n******* Resultado redondeado a 2 espacios decimales *******\nLa recta que mejor se ajusta es la siguiente:\n" \
f"Y = {m:.2f}x + {b:.2f}.\n" \
f"m = {m:.2f}\n" \
f"b = {b:.2f}\n")
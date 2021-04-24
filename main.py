from polinomio import Polinomio

# Leer grado
grado = int(input("Introduce el grado del polinomio: "))

# Pedir los coeficientes del polinomio, comenzando por el término independiente
print("Introduce los coeficientes del polinomio comenzando por el término independiente\n"+
		"Coeficientes:")
coeficientes = []

for i in range(grado+1):
	coeficiente = float(input(f"a[{i}]: "))
	coeficientes.append(coeficiente)

print()

# Leer intervalos
a = float(input("Introduce el inicio del intervalo: a = "))
b = float(input("Introduce el fin del intervalo: b = "))

# Leer cifras significativas
cifras_significativas = int(input("Introduce la cantidad de cifras significativas: "))
print()

# Leer regla de integración aproximada
print("Elige la regla de integración aproximada: \n 1. Trapecio \n 2. Simpson 1/3.")
regla = int(input("Introduce el número de la opción deseada: "))
print()

# Tolerancia al error relativo normalizado porcentual ERNP
tolerancia = 0.5*pow(10, 2 - cifras_significativas)

p = Polinomio(coeficientes, grado)

long_arc = 0.0
subintervalos = 0

if regla == 1:
    long_arc, subintervalos = p.long_arc_trapecio(a, b, tolerancia)
elif regla == 2:
    long_arc, subintervalos = p.long_arc_simpson13(a, b, tolerancia)

long_arc = round(long_arc, cifras_significativas)

print(f"Longitud de arco: {long_arc}")
print(f"Subintervalos: {subintervalos}")
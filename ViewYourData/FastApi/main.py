import math
import numpy as np

'''
resultado = ((7.6**3.7) - (8.2 * math.sqrt(24.5)))
print(resultado)
'''

'''
#Total de cada articulo
articulos = np.array([13200, 29730, 135000, 65800])

# Porcentajes de Bogotá (tabla)
porcentajes = np.array([0.20, 0.45, 0.23, 0.80])

#Costo de pdruccion
costo_produccion = np.array([5000, 3200, 2500, 1800 ])

#Produccion bogota
produccion_bogota = articulos * porcentajes

#Costo total
costo_bogota = produccion_bogota * costo_produccion

costo_total_bogota = np.sum(costo_bogota)

print(costo_total_bogota)
'''
#Ecuación

coeficientes = [50, 95, -18, -72]
# Encontrar raíces
raices = np.roots(coeficientes)


# Ordenar en orden ascendente
raices_ordenadas = np.sort(raices)

# Mostrar solo soluciones reales
soluciones_reales = [r.real for r in raices_ordenadas if np.isreal(r)]

# Imprimir resultados
print(f"x1 = {soluciones_reales[0]:.6f}")
print(f"x2 = {soluciones_reales[1]:.6f}")
print(f"x3 = {soluciones_reales[2]:.6f}")

# Valor de x
x = 3.069

# Aplicamos el Teorema de Pitágoras
y = np.sqrt(x**2 + 12**2)
z = np.sqrt((30 - x)**2 + 28**2)

# Longitud total del cable
W = y + z

# Imprimir resultado
print(f"La longitud total del cable es: {W:.4f} ft")
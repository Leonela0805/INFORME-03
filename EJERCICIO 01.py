# Realizar operaciones de unión, intersección y diferencia de conjuntos.
def crear_conjunto():
    n = int(input('Cantidad de elementos del conjunto: '))
    c = {'a'}
    for i in range(1,n):
        dato = input('Ingresar un elemento del conjunto: ')
        c.add(dato)
    return c

conjunto1 = crear_conjunto()
print('El conjunto uno es: ', conjunto1)
conjunto2 = crear_conjunto()
print('El conjunto dos es: ', conjunto2)
conjunto3 = crear_conjunto()
print('El conjunto tres es: ', conjunto3)

# Unión de conjuntos:
def unir_conjuntos(c1,c2,c3):
    c = c1.union(c2)
    respuesta = c.union(c3)
    print('La unión de los conjuntos es: ', respuesta)

unir_conjuntos(conjunto1,conjunto2,conjunto3)

# Intersección de conjuntos:
def interseccion_conjuntos(c1,c2,c3):
    c = c1.intersection(c2)
    respuesta = c.intersection(c3)
    print('La intersección de los conjuntos es: ', respuesta)

interseccion_conjuntos(conjunto1,conjunto2,conjunto3)

# Diferencia de conjuntos:
def diferencia_conjuntos(c1,c2):
    diferencia = c1 - c2
    print('La diferencia entre {} y {} es: {}'.format(c1,c2,diferencia))

diferencia_conjuntos(conjunto1,conjunto2)
diferencia_conjuntos(conjunto2,conjunto1)
diferencia_conjuntos(conjunto3,conjunto2)
diferencia_conjuntos(conjunto2,conjunto3)
diferencia_conjuntos(conjunto1,conjunto3)
diferencia_conjuntos(conjunto3,conjunto1)

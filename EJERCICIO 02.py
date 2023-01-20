# Calcular la diferencia entre dos conjuntos.
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

def diferencia_conjuntos(c1,c2):
    diferencia = c1 - c2
    print('La diferencia entre {} y {} es: {}'.format(c1,c2,diferencia))

diferencia_conjuntos(conjunto1,conjunto2)
diferencia_conjuntos(conjunto2,conjunto1)
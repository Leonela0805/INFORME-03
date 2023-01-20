# Calcular la diferencia simétrica entre 3 conjuntos.
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

# Diferencia simétrica
def diferencia_simetrica(c1,c2,c3):
    diferencia = c1.symmetric_difference(c2)
    print('La diferencia simétrica  de los conjuntos {} y {} es: '.format(c1,c2), diferencia)
    respuesta = diferencia.symmetric_difference(c3)
    print()
    print('La diferencia simétrica de los conjuntos {} y {} es: '.format(diferencia,c3), respuesta)

print()
print('La diferenca simétrica de los conjuntos en el orden conjunto1, conjunto2, conjunto3 es:')
diferencia_simetrica(conjunto1,conjunto2,conjunto3)

print()
print('La diferenca simétrica de los conjuntos en el orden conjunto3, conjunto2, conjunto1 es:')
diferencia_simetrica(conjunto3,conjunto2,conjunto1)
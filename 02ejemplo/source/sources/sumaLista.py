"""
Suma de los elementos de una lista en python
============================================
En este modulo veras como podemos sumas los elementos que se encuentren
dentro de una lista por medio de una funcion que recibe como parametro
dicha lista
"""
def sumaLista(list):
    """
    **Esta funcion recibe una lista y acomula la sumatoria recorriendo
    cada elemento y al final retorna el total acumulado**
    """
    suma = 0
    for num in list:
        suma+=num
    return suma
"""
**Definicion de la lista**
"""
lista = [2,3,1,2,3,4]
print(sumaLista(lista))
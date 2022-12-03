'''
4. (diofantina) Programa que lê três números inteiros positivos a, b, c, com mdc(a, b) =
1 e determina a solução mínima x, y inteira para equação ax + by = c.
'''

# calcular mdc com teorema de euclides
def mdc_euclides(a, b):

    anterior  = a
    atual     = b

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual
        anterior = atual
        atual = resto

    return anterior


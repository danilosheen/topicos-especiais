'''
(mdc-euclides) Dados dois números inteiros positivos, determinar o máximo divisor
comum entre eles usando o algoritmo de Euclides.
'''
print("Informe o valor de A e B: ", end='')
a, b = map(int, input().split())

def mdc_euclides():

    anterior  = a
    atual     = b

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual
        anterior = atual
        atual = resto

    return anterior

print("MDC de {} e {} = {}".format(a, b, mdc_euclides()))

'''
(mdc-euclides) Dados dois números inteiros positivos, determinar o máximo divisor
comum entre eles usando o algoritmo de Euclides.
'''
def mdc_euclides(a, b):

    anterior  = a
    atual     = b

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual
        anterior = atual
        atual = resto

    return anterior

print("Informe o valor de A e B: ", end='')
a, b = map(int, input().split())
print("MDC de {} e {} = {}".format(a, b, mdc_euclides(a, b)))

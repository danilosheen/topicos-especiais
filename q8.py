'''
(sistema-invertiveis) Programa que lê um número inteiro positivo n e determina
seu Conjunto de Invertíveis Módulo n, ou seja, {b1, b2, · · · , bφ(n)} tal que bi ≡ bj
(mod n) implica i = j.
'''

def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

def invertiveis(n):
    invertiveis = []
    for i in range(1, n):
        if euclides(i, n) == 1:
            invertiveis.append(i)
    return invertiveis

n = int(input("Informe o valor de n: "))
invertiveis = invertiveis(n)
print(invertiveis)
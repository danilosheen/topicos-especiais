
'''
(inverso) Programa que lê dois números inteiros positivos n e a, com mdc(n, a) = 1
e determina seu inverso b, ou seja, um inteiro b tal que ab˙ ≡ 1 (mod n).
'''
import math

# lê os números n e a

n = int(input("Digite o valor de n: "))
a = int(input("Digite o valor de a: "))

# verifica se o mdc(n, a) é 1
if math.gcd(n, a) != 1:
    print("O inverso não existe pois o mdc(n, a) não é 1")
else:
    # inicializa os valores de x e y
    x, y = 0, 1
    b = n

    # executa o algoritmo de Euclides estendido
    while a != 0:
        q, b, a = b // a, a, b % a
        x, y = y - q * x, x

    # se o resultado for negativo, adiciona n
    if x < 0:
        x += n

    # imprime o inverso
    print("O inverso de a é", x)

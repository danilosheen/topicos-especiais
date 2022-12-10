'''
4. (diofantina) Programa que lê três números inteiros positivos a, b, c, com mdc(a, b) =
1 e determina a solução mínima x, y inteira para equação ax + by = c.
'''

def euclides_estendido(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = euclides_estendido(b, a % b)
        return (d, y, x - y * (a // b))

def solucao_minima(a, b, c):
    d, x, y = euclides_estendido(a, b)
    if c % d != 0:
        return None
    else:
        x *= c // d
        y *= c // d
        return (x, y)

a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

x, y = solucao_minima(a, b, c)
print(f"x = {x}, y = {y}")
    



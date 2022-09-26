'''
(mdc) Programa que lê dois inteiro positivos a e b 
 e imprime o máximo divisor comum (mdc) de a e b.
'''
def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a 

print("Informe o valor de A e B: ", end='')
a, b = map(int, input().split())
print("MDC de {} e {} = {}".format(a, b, mdc(a,b)))

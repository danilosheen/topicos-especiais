def mdc(a,b):
    while b !=0:
        resto = a % b
        a = b
        b = resto

    return a 

print("informe o valor de A e B: ", end='')
a, b = map(int, input().split())
print("MDC de {} e {} = {}".format(a, b, mdc(a,b)))

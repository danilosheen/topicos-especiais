'''
 (ordem) Programa que lê dois números inteiros positivos n, a, com mdc(n, a) = 1
e determina o menor tal que a^0 ≡ 1 (mod n).
'''

# Função para calcular o MDC de dois números inteiros a e b
def mdc(a, b):
  # Se b = 0, então o MDC de a e b é a
  if b == 0:
    return a
  
  # Senão, o MDC de a e b é o MDC de b e o resto da divisão inteira de a por b
  return mdc(b, a % b)

# Função para calcular o número de inteiros positivos menores que n que são coprimos com n
def euler(n):
  # Inicialmente, ϕ(n) é igual a n
  phi = n

  # Verifica todos os números primos que dividem n
  for p in range(2, n + 1):
    # Se o número primo p divide n, então atualiza o valor de ϕ(n)
    if n % p == 0:
      phi = phi * (1 - 1/p)

  # Retorna o valor de ϕ(n)
  return phi

# Função para calcular o menor inteiro positivo tal que a^0 ≡ 1 (mod n)
def ordem(a, n):
  # Verifica se o MDC de n e a é igual a 1
  if mdc(n, a) != 1:
    raise ValueError("O MDC de n e a deve ser igual a 1")

  # Calcula o valor de ϕ(n)
  phi = euler(n)

  # Calcula e retorna o valor da ordem de a módulo n
  return phi / mdc(phi, a)

# Lê os valores de n e a
n = int(input("Insira o valor de n: "))
a = int(input("Insira o valor de a: "))

# Calcula e imprime o menor inteiro positivo tal que a^0 ≡ 1 (mod n)
print("ordem(a, n) =", ordem(a, n))

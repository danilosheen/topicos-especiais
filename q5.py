'''
. (funcao-euler) Programa que lê um número inteiro positivo n e determina ϕ(n).
'''

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

# Lê o valor de n
n = int(input("Insira o valor de n: "))

# Calcula e imprime o número de inteiros positivos menores que n que são coprimos com n
print("ϕ(n) =", euler(n))

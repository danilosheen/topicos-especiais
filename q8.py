'''
(sistema-invertiveis) Programa que lê um número inteiro positivo n e determina
seu Conjunto de Invertíveis Módulo n, ou seja, {b1, b2, · · · , bφ(n)} tal que bi ≡ bj
(mod n) implica i = j.
'''

# Importa a biblioteca math para calcular o valor de phi(n)
import math

# Função para calcular o valor de phi(n)
def phi(n):
  # Inicializa o contador de coprimos
  count = 0

  # Percorre todos os inteiros i entre 1 e n
  for i in range(1, n + 1):
    # Verifica se i é coprimo com n
    if math.gcd(i, n) == 1:
      # Incrementa o contador de coprimos
      count += 1

  # Retorna o valor de phi(n)
  return count

# Solicita ao usuário que informe o valor de n
n = int(input("Informe o valor de n: "))

# Calcula o valor de phi(n)
phi_n = phi(n)

# Cria uma lista vazia para armazenar o conjunto de invertíveis módulo n
invertiveis = []

# Percorre todos os inteiros i entre 1 e n
for i in range(1, n + 1):
  # Verifica se i é coprimo com n
  if math.gcd(i, n) == 1:
    # Adiciona i à lista de invertíveis módulo n
    invertiveis.append(i)

# Exibe o conjunto de invertíveis módulo n para o usuário
print("O conjunto de invertíveis módulo n é:", invertiveis)

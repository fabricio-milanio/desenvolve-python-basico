import random
import math

n = random.randint(0, 100)

print(f"\nO programa decidiu somar {n} valores aleatórios.")

soma_dos_valores = 0
for _ in range(n):
    numero_aleatorio = random.randint(0, 100)
    soma_dos_valores += numero_aleatorio

raiz_quadrada_da_soma = math.sqrt(soma_dos_valores)

print(f"\nA soma dos {n} valores gerados é: {soma_dos_valores}")
print(f"\nA raiz quadrada da soma é: {raiz_quadrada_da_soma:.2f}\n")
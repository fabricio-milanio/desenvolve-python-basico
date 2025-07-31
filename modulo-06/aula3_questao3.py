'''
Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente.
Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]

Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]
'''

import random

numeros = [random.randint(-10, 10) for _ in range(20)]

maior_comprimento = 0
inicio_maior_intervalo = -1
comprimento_atual = 0
inicio_atual = -1

for i, num in enumerate(numeros):
    if num < 0:
        if comprimento_atual == 0:
            inicio_atual = i
        comprimento_atual += 1
    else:
        if comprimento_atual > maior_comprimento:
            maior_comprimento = comprimento_atual
            inicio_maior_intervalo = inicio_atual
        comprimento_atual = 0

if comprimento_atual > maior_comprimento:
    maior_comprimento = comprimento_atual
    inicio_maior_intervalo = inicio_atual

print(f"Original: {numeros}")

if inicio_maior_intervalo != -1:
    fim_maior_intervalo = inicio_maior_intervalo + maior_comprimento
    del numeros[inicio_maior_intervalo:fim_maior_intervalo]

print(f"Editada:  {numeros}")
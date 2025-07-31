'''
Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores),
os armazena em uma lista e, usando fatiamento de listas, imprima:

A lista original

Os 3 primeiros elementos

Os 2 últimos elementos

A lista invertida (do fim para o começo)

Os elementos de índice par (0, 2, 4 … )

Os elementos de índice ímpar (1, 3, 5, … )
'''

numeros = []

print("Digite 4 números inteiros:")

for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(valor)

print("\nAnálise da lista atual")
print(f"Lista atual: {numeros}")
print(f"Os 3 primeiros elementos: {numeros[:3]}")
print(f"Os 2 últimos elementos: {numeros[-2:]}")
print(f"Lista invertida: {numeros[::-1]}")
print(f"Elementos de índice par: {numeros[::2]}")
print(f"Elementos de índice ímpar: {numeros[1::2]}")
'''
Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
Exemplo de interação via terminal (entradas em laranja): 
Digite a quantidade de elementos da lista 1: 4

Digite os 4 elementos da lista 1:

1
2
3
4

Digite a quantidade de elementos da lista 2: 6

Digite os 6 elementos da lista 2:

5
6
7
8
9
10

Lista intercalada: 1 5 2 6 3 7 4 8 9 10
'''

lista1 = []
lista2 = []
lista_intercalada = []

qtd_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtd_lista1} elementos da lista 1:")
for _ in range(qtd_lista1):
    elemento = int(input())
    lista1.append(elemento)

qtd_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd_lista2} elementos da lista 2:")
for _ in range(qtd_lista2):
    elemento = int(input())
    lista2.append(elemento)

tamanho_menor_lista = min(len(lista1), len(lista2))

for i in range(tamanho_menor_lista):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[tamanho_menor_lista:])
elif len(lista2) > len(lista1):
    lista_intercalada.extend(lista2[tamanho_menor_lista:])

resultado_formatado = " ".join(map(str, lista_intercalada))
print(f"Lista intercalada: {resultado_formatado}")
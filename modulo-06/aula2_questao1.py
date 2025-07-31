'''
Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

A lista ordenada, sem modificar a lista original

A lista original

O índice do maior valor da lista

O índice do menor valor da lista
'''

import random

lista = [random.randint(-100, 100) for _ in range(20)]

print("Lista ordenada:", sorted(lista))
print("Lista original:", lista)
print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))
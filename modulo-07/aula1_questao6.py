'''
Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

Digite a palavra objetivo: amor

Anagramas: ["amor", "mora", "ramo", "Roma"] 
'''

import collections

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()
anagramas = []
objetivo_ordenado = sorted(palavra_objetivo.lower())

for palavra in palavras:
    if sorted(palavra.lower()) == objetivo_ordenado:
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
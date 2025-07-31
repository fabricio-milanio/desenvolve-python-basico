'''
Solicite uma frase do usuário e usando compreensão de listas imprima:

A lista de vogais da frase, ordenada alfabeticamente

A lista de consoantes da frase (remova espaços em branco)

Digite uma frase: Eu gosto de programar em Python

Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']

Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']
'''

frase = input("Digite uma frase: ")

vogais_ref = "aeiou"

vogais = sorted([letra.lower() for letra in frase if letra.lower() in vogais_ref])

consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in vogais_ref]

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
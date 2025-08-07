'''
Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:

Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

19 vogais

Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]
'''

frase = input("Digite uma frase: ")
vogais = "aeiou"
indices_vogais = []
contador_vogais = 0
for i, letra in enumerate(frase.lower()):
    if letra in vogais:
        indices_vogais.append(i)
        contador_vogais += 1
print(f"{contador_vogais} vogais")
print(f"Índices {indices_vogais}")
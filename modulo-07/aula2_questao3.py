'''
Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo
(ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere
maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

Digite uma frase (digite "fim" para encerrar): Radar

"Radar" é palíndromo

Digite uma frase (digite "fim" para encerrar): Bom dia!

"Bom dia!" não é palíndromo

Digite uma frase (digite "fim" para encerrar): Ame o poema

"Ame o poema" é palíndromo

Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!

"A Daniela ama a lei? Nada!" é palíndromo

Digite uma frase (digite "fim" para encerrar): fim
'''

import string

while True:
    frase_original = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase_original.lower() == "fim":
        break

    frase_limpa = ''.join(char for char in frase_original.lower() if char.isalnum())
    
    frase_reversa = frase_limpa[::-1]

    if frase_limpa == frase_reversa:
        print(f'"{frase_original}" é palíndromo')
    else:
        print(f'"{frase_original}" não é palíndromo')
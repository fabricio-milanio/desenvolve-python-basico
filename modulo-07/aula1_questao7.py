'''
Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados,
bem como a chave da criptografia. Regras:

Chave de criptografia: gere um valor n aleatório entre 1 e 10

Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres
visíveis (entre 33 e 126 na tabela Unicode)

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

chave_aleatoria = 5

nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']
'''

import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []
    
    inicio_intervalo = 33
    fim_intervalo = 126
    tamanho_intervalo = fim_intervalo - inicio_intervalo + 1

    for nome in nomes:
        nome_cript = ""
        for char in nome:
            ord_original = ord(char)
            if inicio_intervalo <= ord_original <= fim_intervalo:
                indice = ord_original - inicio_intervalo
                novo_indice = (indice + chave) % tamanho_intervalo
                novo_char = chr(novo_indice + inicio_intervalo)
                nome_cript += novo_char
            else:
                nome_cript += char
        nomes_criptografados.append(nome_cript)
        
    return nomes_criptografados, chave

# Exemplo de uso:
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print(f"nomes = {nomes}")
print(f"chave_aleatoria = {chave_aleatoria}")
print(f"nomes_cript = {nomes_cript}")
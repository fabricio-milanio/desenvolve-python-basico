'''
Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:

Pelo menos 8 caracteres de comprimento.

Contém pelo menos uma letra maiúscula e uma letra minúscula.

Contém pelo menos um número.

Contém pelo menos um caractere especial (por exemplo, @, #, $).

def validador_senha(senha):

    #### Escreva a função


# Exemplo de uso:

senha1 = "Senha123@"

senha2 = "senhafraca"

senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True

print(validador_senha(senha2))  # Saída esperada: False

print(validador_senha(senha3))  # Saída esperada: False
'''

import string

def validador_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    caracteres_especiais = string.punctuation

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in caracteres_especiais:
            tem_especial = True
            
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))
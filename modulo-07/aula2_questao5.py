'''
Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com
as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
Dica: use a biblioteca random.

def embaralhar_palavras(frase):

    #### Escreva a função


# Exemplo de uso:

frase = "Python é uma linguagem de programação"

resultado = embaralhar_palavras(frase)

print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"
'''

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    
    for palavra in palavras:
        if len(palavra) > 3:
            miolo = list(palavra[1:-1])
            random.shuffle(miolo)
            palavra_embaralhada = palavra[0] + ''.join(miolo) + palavra[-1]
            nova_frase.append(palavra_embaralhada)
        else:
            nova_frase.append(palavra)
            
    return ' '.join(nova_frase)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
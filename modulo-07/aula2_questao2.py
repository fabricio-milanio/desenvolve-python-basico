'''
Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

Digite uma frase: O rato roeu a roupa do rei

Frase modificada: * r*t* r*** * r**p* d* r**
'''

frase_original = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
frase_modificada = ""

for letra in frase_original:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra

print("Frase modificada:", frase_modificada)
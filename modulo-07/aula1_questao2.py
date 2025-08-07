'''
Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente.
Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

Digite seu primeiro nome: Alice

Digite seu sobrenome: Silva

Bem-vinda, Alice Silva! 
'''

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = primeiro_nome + " " + sobrenome
print("Bem-vindo(a), " + nome_completo + "!")
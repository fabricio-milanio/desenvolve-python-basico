'''
Reescreva o código a seguir para construir a lista aprovados usando compreensão de listas, ou seja, eliminando o laço de repetição.

alunos = ["Maria", "Jose", "Carla", "Sol"]

notas = [35, 50, 20, 80]

aprovados = []

for i in range(len(notas)):

if notas[i] >= 60:

aprovados.append(alunos[i]) 
'''

alunos = ["Maria", "Jose", "Carla", "Sol", "Lia"]
notas = [35, 50, 20, 80, 75]

print("Aluno(s) aprovado(s):", ", ".join([aluno for aluno, nota in zip(alunos, notas) if nota >= 60]))
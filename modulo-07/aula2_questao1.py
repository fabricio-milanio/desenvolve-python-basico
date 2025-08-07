'''
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
Dica: usando listas você não precisa fazer um "if" para cada mês.

Digite uma data de nascimento: 29/10/1973

Você nasceu em  29 de Outubro de 1973.
'''

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

partes = data_nascimento.split('/')
dia = partes[0]
mes_numero = int(partes[1])
ano = partes[2]

meses_por_extenso = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

nome_do_mes = meses_por_extenso[mes_numero - 1]

print(f"Você nasceu em {dia} de {nome_do_mes} de {ano}.")
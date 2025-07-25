'''
3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro.
Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos
de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve
imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e
já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir
False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas
de dados destacadas em laranja e as impressões de seu código em branco.
'''

idade = int(input("Digite sua idade: "))
jogos_jogados = input("Você já jogou pelo menos 3 jogos de tabuleiro? Digite true se sim ou false se não: ")
jogos_jogados = jogos_jogados.lower() == "true"
vitorias = int(input("Quantas vezes você venceu um jogo? "))
pode_ingressar = (16 <= idade <= 18) and jogos_jogados and (vitorias >= 1)

print(pode_ingressar)
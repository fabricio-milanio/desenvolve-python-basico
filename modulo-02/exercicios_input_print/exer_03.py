'''
3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando
a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e
imprima ao final o preço total da compra. Note no exemplo a seguir que:

Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)

A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).

Entrada

Saída

Digite o nome do produto 1:calça

Digite o preço unitário do produto 1:199.90

Digite a quantidade do produto 1: 3

Digite o nome do produto 2:camisa

Digite o preço unitário do produto 2:49.95

Digite a quantidade do produto 2:10

Digite o nome do produto 3:cinto

Digite o preço unitário do produto 3:25

Digite a quantidade do produto 3:3

'''

prod1 = input("Digite o nome do produto: ")
val_prod1 = float(input("Digite o preço unitário do produto: "))
qtd_prod1 = int(input("Digite a quantidade do produto: "))
val_tot_prod1 = val_prod1 * qtd_prod1

prod2 = input("Digite o nome do produto: ")
val_prod2 = float(input("Digite o preço unitário do produto: "))
qtd_prod2 = int(input("Digite a quantidade do produto: "))
val_tot_prod2 = val_prod2 * qtd_prod2

prod3 = input("Digite o nome do produto: ")
val_prod3 = float(input("Digite o preço unitário do produto: "))
qtd_prod3 = int(input("Digite a quantidade do produto: "))
val_tot_prod3 = val_prod3 * qtd_prod3

val_tot_prods = val_tot_prod1 + val_tot_prod2 + val_tot_prod3

print(f"Total: R${val_tot_prods:.2f}.")
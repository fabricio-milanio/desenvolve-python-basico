'''
4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e
calcule a menor quantidade possível de notas necessárias para pagar aquele valor.
As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

Entrada

Saída

576

5 nota(s) de R$100,00

1 nota(s) de R$50,00

1 nota(s) de R$20,00

0 nota(s) de R$10,00

1 nota(s) de R$5,00

0 nota(s) de R$2,00

1 nota(s) de R$1,00

'''

valor = int(input("Digite o valor em reais: "))
nota100 = valor // 100      # Calcula o número de notas de 100
valor = valor % 100         # Atualiza o valor restante após retirar as notas de 100
nota50 = valor // 50        # Calcula o número de notas de 50
valor = valor % 50          # Atualiza o valor restante após retirar as notas de 50
nota20 = valor // 20        # Calcula o número de notas de 20
valor = valor % 20          # Atualiza o valor restante após retirar as notas de 20
nota10 = valor // 10        # Calcula o número de notas de 10
valor = valor % 10          # Atualiza o valor restante após retirar as notas de 10
nota5 = valor // 5          # Calcula o número de notas de 5
valor = valor % 5           # Atualiza o valor restante após retirar as notas de 5
nota2 = valor // 2          # Calcula o número de notas de 2
valor = valor % 2           # Atualiza o valor restante após retirar as notas de 2
nota1 = valor // 1          # Calcula o número de notas de 1

print(f"{nota100} nota(s) de R$100,00")
print(f"{nota50} nota(s) de R$50,00")
print(f"{nota20} nota(s) de R$20,00")
print(f"{nota10} nota(s) de R$10,00")
print(f"{nota5} nota(s) de R$5,00")
print(f"{nota2} nota(s) de R$2,00")
print(f"{nota1} nota(s) de R$1,00")
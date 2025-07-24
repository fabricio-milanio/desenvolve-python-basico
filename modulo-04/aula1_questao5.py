n = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0

for i in range(n):
    idade = int(input(f"Digite a idade do respondente {i + 1}: "))
    soma_idades += idade

if n > 0:
    media = soma_idades / n
    print(f"A média das idades é: {media}")
else:
    print("Nenhuma idade foi inserida para o cálculo.")
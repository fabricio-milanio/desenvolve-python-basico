import random

numero_secreto = random.randint(1, 10)

while True:
    try:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
        if palpite < numero_secreto:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_secreto:
            print("Muito alto, tente novamente!")
        else:
            print(f"Correto! O número é {numero_secreto}.")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
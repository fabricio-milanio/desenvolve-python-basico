import random

caminho_enforcado = r'C:\Users\PDITA3396W\OneDrive\Desktop\Projeto Desenvolve\phyton\desenvolve-python-basico\modulo-07\gabarito_enforcado.txt'
caminho_forca = r'C:\Users\PDITA3396W\OneDrive\Desktop\Projeto Desenvolve\phyton\desenvolve-python-basico\modulo-07\gabarito_forca.txt'

with open(caminho_enforcado, "r", encoding="utf-8") as f:
    conteudo = f.read()
estagios_brutos = conteudo.split('=========\n')
estagios = []
for bloco in estagios_brutos:
    if bloco.strip() or '---' in bloco:
        estagio_completo = bloco.strip('\n') + '\n=========\n'
        estagios.append(estagio_completo)

with open(caminho_forca, "r", encoding="utf-8") as f:
    palavras = [linha.strip().lower() for linha in f.readlines()]

palavra_secreta = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra_secreta)
erros = 0
letras_erradas = []
letras_tentadas = []
venceu = False

print("--- Bem-vindo ao Jogo da Forca! ---")

while erros < 6 and not venceu:
    print(estagios[erros])
    print("Palavra: ", " ".join(letras_descobertas))
    
    if letras_erradas:
        print("Letras erradas: ", " ".join(sorted(letras_erradas)))
    
    if "_" not in letras_descobertas:
        venceu = True
        continue

    tentativa = input("Digite uma letra: ").lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("\nEntrada inválida. Por favor, digite apenas uma letra.")
        continue

    if tentativa in letras_tentadas:
        print("\nVocê já tentou essa letra. Tente outra.")
        continue
    
    letras_tentadas.append(tentativa)

    if tentativa in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                letras_descobertas[i] = letra
        print("\nBom palpite!\n")
    else:
        erros += 1
        letras_erradas.append(tentativa)
        if erros < 6:
            print(f"\nLetra '{tentativa}' não encontrada. Você tem {6 - erros} tentativa(s) restante(s).")

if venceu:
    print("\nParabéns! Você adivinhou a palavra!")
    print(f"A palavra era: {palavra_secreta.upper()}")
else:
    print(estagios[erros])
    print("\nVocê foi enforcado!")
    print(f"A palavra secreta é: {palavra_secreta.upper()}")
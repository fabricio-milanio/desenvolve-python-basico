n = int(input("Digite a quantidade de experimentos: "))

total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(n):
    prompt = f"Dados do experimento {i + 1} (ex: 10 C): "
    linha = input(prompt).split()
    
    quantia = int(linha[0])
    tipo = linha[1].upper()

    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

total_geral = total_coelhos + total_ratos + total_sapos

print(f"\n--- RELATÓRIO FINAL ---")
print(f"Total: {total_geral} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")

if total_geral == 0:
    p_coelhos = 0.0
    p_ratos = 0.0
    p_sapos = 0.0
else:
    p_coelhos = (total_coelhos / total_geral) * 100
    p_ratos = (total_ratos / total_geral) * 100
    p_sapos = (total_sapos / total_geral) * 100

print(f"Percentual de coelhos: {p_coelhos:.2f} %")
print(f"Percentual de ratos: {p_ratos:.2f} %")
print(f"Percentual de sapos: {p_sapos:.2f} %")
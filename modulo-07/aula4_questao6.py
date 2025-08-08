import csv

caminho_arquivo = r'C:\Users\PDITA3396W\OneDrive\Desktop\Projeto Desenvolve\phyton\desenvolve-python-basico\modulo-07\spotify-2023.csv'

print("--- As 5 primeiras linhas do arquivo ---")
with open(caminho_arquivo, mode='r', encoding='latin-1') as arquivo:
    leitor = csv.reader(arquivo)
    print(next(leitor))
    print(next(leitor))
    print(next(leitor))
    print(next(leitor))
    print(next(leitor))
print("-" * 38 + "\n")

musicas_mais_tocadas = {}

with open(caminho_arquivo, mode='r', encoding='latin-1') as arquivo:
    leitor = csv.reader(arquivo)
    cabecalho = next(leitor)

    for linha in leitor:
        if len(linha) < 9:
            continue

        track_name = linha[0]
        artists_name = linha[1]
        year_str = linha[3]
        streams_str = linha[8]

        if not year_str.isdigit() or not streams_str.isdigit():
            continue
            
        if '"' in track_name or '"' in artists_name:
            continue

        released_year = int(year_str)
        streams = int(streams_str)
        
        if 2012 <= released_year <= 2022:
            if released_year not in musicas_mais_tocadas or streams > musicas_mais_tocadas[released_year][3]:
                musicas_mais_tocadas[released_year] = [track_name, artists_name, released_year, streams]

lista_final = []
for ano in sorted(musicas_mais_tocadas.keys()):
    lista_final.append(musicas_mais_tocadas[ano])

print("--- Lista das músicas mais tocadas por ano (2012-2022) ---")

for musica in lista_final:
    print(musica)
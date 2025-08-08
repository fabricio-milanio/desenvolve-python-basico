import re

caminho_do_arquivo = r'C:\Users\PDITA3396W\OneDrive\Desktop\Projeto Desenvolve\phyton\desenvolve-python-basico\modulo-07\estomago.txt'

try:
    with open(caminho_do_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()
    
    conteudo_completo = "".join(linhas)

    print("---- Análise do Roteiro 'Estômago' ----")
    
    print("\n>> As primeiras 25 linhas do arquivo:\n")
    for linha in linhas[:25]:
        print(linha, end="")
    
    num_linhas = len(linhas)
    print(f"\n\n>> O arquivo tem {num_linhas} linhas.")
    
    if linhas:
        linha_mais_longa = max(linhas, key=lambda linha: len(linha.strip()))
        print("\n>> A linha com maior número de caracteres é:\n")
        print(linha_mais_longa.strip())
    
    contagem_nonato = len(re.findall(r'\bnonato\b', conteudo_completo, re.IGNORECASE))
    contagem_iria = len(re.findall(r'\bíria\b', conteudo_completo, re.IGNORECASE))
    
    print("\n>> Contagem de personagens:")
    print(f"O nome 'Nonato' é mencionado {contagem_nonato} vezes.")
    print(f"O nome 'Íria' é mencionado {contagem_iria} vezes.")
    print("\n------------------------------------------")

except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado no caminho especificado.")
    print(f"Caminho: {caminho_do_arquivo}")
    print("Por favor, verifique se o caminho está correto e se o arquivo existe no local.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")
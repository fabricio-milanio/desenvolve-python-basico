import re

with open("frase.txt", "r") as f_leitura:
    conteudo = f_leitura.read()

palavras = conteudo.split()
palavras_limpas = []

for palavra in palavras:
    palavra_limpa = re.sub(r'[^a-zA-ZáéíóúâêîôûàèìòùãõçÁÉÍÓÚÂÊÎÔÛÀÈÌÒÙÃÕÇ]', '', palavra)
    if palavra_limpa:
        palavras_limpas.append(palavra_limpa)

with open("palavras.txt", "w") as f_escrita:
    texto_final = "\n".join(palavras_limpas)
    f_escrita.write(texto_final)

with open("palavras.txt", "r") as f_final:
    print(f_final.read())
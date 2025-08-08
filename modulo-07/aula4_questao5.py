import csv

nome_do_arquivo = "meus_livros.csv"

cabecalho = ["Título", "Autor", "Ano de publicação", "Número de páginas"]

livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["1984", "George Orwell", 1949, 328],
    ["A Hora da Estrela", "Clarice Lispector", 1977, 88],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["O Quinze", "Rachel de Queiroz", 1930, 208],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 576],
    ["Ensaio sobre a Cegueira", "José Saramago", 1995, 310],
    ["Fahrenheit 451", "Ray Bradbury", 1953, 256],
]

with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(cabecalho)
    escritor.writerows(livros)

print(f"Arquivo '{nome_do_arquivo}' foi criado com sucesso.")
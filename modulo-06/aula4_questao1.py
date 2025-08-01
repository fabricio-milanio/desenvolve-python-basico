'''
Escreva um script python que use compreensão de listas para criar as seguintes listas:

Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]

Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]

Todos os números entre 1 e 100 que sejam divisíveis por 7

Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar']) 
'''

pares_20_a_50 = [numero for numero in range(20, 51, 2)]
print(f"Pares entre 20 e 50: {pares_20_a_50}")

quadrados_1_a_9 = [numero**2 for numero in range(1, 10)]
print(f"Quadrados de 1 a 9: {quadrados_1_a_9}")

divisiveis_por_7 = [numero for numero in range(7, 101, 7)]
print(f"Números entre 1 e 100 divisíveis por 7: {divisiveis_por_7}")

paridade_range = ["par" if numero % 2 == 0 else "ímpar" for numero in range(0, 30, 3)]
print(f"Paridade para range(0, 30, 3): {paridade_range}")
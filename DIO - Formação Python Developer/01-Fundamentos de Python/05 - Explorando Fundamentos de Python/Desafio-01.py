"""
Descrição

Neste desafio, você deve escreva uma solução que
receba um número inteiro como entrada e
determine se ele é par ou ímpar. Dessa forma, a
solução deve retornar uma string indicando Par se o
número for par e Ímpar se o número for ímpar

Entrada	Saída
2	Par
5	Ímpar
6	Par
"""

print(f"""======== Vamos descrobir se um número é ===========
===========    Par ou Ímpar       ===========""")

valor = int(input("Digite um número:\n"))
if valor % 2 ==0:
    print(f"O número {valor} é par.")
else:
    print(f"O número {valor} é ímpar.")

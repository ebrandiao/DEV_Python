"""
5.	Escreva um programa que indique se um arquivo existe ou não.
Caso exista, indique se é realmente um arquivo ou não.
"""
import os
lista = os.listdir()
lista_arq = []
lista_dir = []

for i in lista:
    if os.path.isfile(i):
        lista_arq.append(i)
    else:
        lista_dir.append(i)

if len(lista_arq) > 0: # checa se tem um arquivo na lista
    print("É um arquivo valido")
    print(" ") # Quebra de linha

if len(lista_dir) > 0:
    print("Não é um aruivo valido")

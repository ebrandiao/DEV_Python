"""
6.	Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path.
"""
import os

lista = os.listdir()

dic_arq = {}
for i in lista:
    if os.path.isfile(i):
        ext = os.path.splitext(i)[1] # Separa em nome e extensão
print(dic_arq)
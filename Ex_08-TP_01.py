"""
8.	Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
"""
import os
lista_dir = []
entrada = input("Entre com o diretório: ")

if os.path.isdir(entrada):
    lista_dir.append(entrada)
    somador = 0
    p_dir = ""
    while lista_dir:
        diretorio = lista_dir[0]
        p_dir = os.path.join(p_dir, diretorio)
        lista = os.listdir(p_dir)
        for i in lista:
            p = os.path.join(p_dir, i)
            if os.path.isdir(p):
                lista_dir.append(i)
            elif os.path.isfile(p):
                somador = somador + os.stat(p).st_size
        lista_dir.remove(diretorio)
    print(str(somador/1000) + "KB")
else:
    print("O diretorio" + p_dir + "não existe")
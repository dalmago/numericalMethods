#!/usr/bin/python
import numpy
"""Tratamento do arquivo pra transformar em uma matriz"""
f = str(input('Numero da matriz: '))
fw = open ("matriz" + f + ".txt", "r")

#n = int(input('Dimensao: '))
n = 10 #dimensao

#e = float(input('Precisao: '))
e = 0.0000001

def transforma_string_lista (linha):
    ls = []
    a = ""
    for caracter in linha:
        if caracter != " " and caracter != "\n":
            a = a + caracter
        else:
            #print (a)
            ls.append (float(a))
            a = ""
    return ls

matriz = [0]*n

for i in range (n):
    linha = fw.readline()
    while linha[0] == "#": #ignora comentario em nova linha
        linha = fw.readline()
    matriz[i] = transforma_string_lista (linha)

linha = fw.readline() #le termo independente B

while linha[0] == "#":
    linha = fw.readline()

exato = fw.readline() #le resposta exata
while exato[0] == "#":
    exato = fw.readline()

fw.close()
exato = transforma_string_lista (exato)
"""ultima linha do arquivo txt 
termo independente B"""
linha = transforma_string_lista (linha) 

for i in range (n):
    matriz[i].append (linha[i])

"""
    Aqui, matriz A[i][j] pronta pra ser usada
"""

def divide_linha (linha, divisor):
    ls = []
    for i in linha:
        ls.append (i/divisor)
    return ls

def soma_linha (linha1, linha2, multiplo2):
    ls = []
    tam = len(linha1)
    for i in range (tam):
        resultado = linha1[i] + multiplo2*linha2[i]
        if abs(resultado) < e:
            resultado = 0
        ls.append (resultado)
    return ls

for i in range (n):
    """
        pivoteamento
    """
    for j in range (i+1, n):
        if abs(matriz[i][i]) < abs(matriz[j][i]):
            matriz[i], matriz[j] = matriz[j], matriz[i]

    """
        diagonal superior
    """

    for j in range (i+1, n):
       matriz[j] = soma_linha (matriz[j], matriz[i],-(matriz[j][i]/matriz[i][i]))


for i in range (n):
    """
        adiciona mais uma coluna a matriz, que vai 
        representar a resposta
    """
    matriz[i].append (0)
"""
    calcula
"""

for i in range (n-1, -1, -1):
    if i == n-1:
        resultado = float(matriz[i][n] / matriz[i][i])
    else:
        resultado = matriz[i][n]
        for j in range (i+1, n):
            resultado = resultado - matriz[i][j]*matriz[j][n+1]
        resultado = float(resultado / matriz[i][i])
    matriz[i][n+1] = resultado
"""
    passa o resultado para uma lista independente
"""
result = []
for i in range (n):
    result.append (matriz[i][n+1])
    matriz[i].pop(n+1)

print ("matriz diagonal superior com pivoteamento e termo\nindependente na ultima coluna:\n")
for i in range (n):
    print (matriz[i])

print ("\nresultado:\n")
print (result)

print ("\nErro absoluto para cada posicao:\n")
EA = []
for i in range (n):
    EA.append (exato[i] - result[i])

print (EA)

print ("\nErro relativo para cada posicao:\n")
ER = []
for i in range (n):
    ER.append (float(EA[i] / exato[i]))

print (ER)

print ("\nMatriz inversa:\n")
A = numpy.matrix(matriz)
print (A.I)


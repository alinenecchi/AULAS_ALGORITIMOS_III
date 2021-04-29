#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY samples as parameter.
#

def largestArea(samples):
    # Write your code here
    square_len = len(samples)
    for i in range(1, square_len):
        for j in range(1, square_len):
            if samples[i][j] == 1:
                samples[i][j] = min(samples[i - 1][j], samples[i][j - 1], samples[i - 1][j - 1]) + 1
            else:
                samples[i][j] = 0
    return max([max(row) for row in samples])

if __name__ == '__main__':

    samples_rows = int(input().strip())
    samples_columns = int(input().strip())

    samples = []

    for _ in range(samples_rows):
        samples.append(list(map(int, input().rstrip().split())))

    result = largestArea(samples)
    print()


'''1. Defeitos do produto Um agente de qualidade é responsável por inspecionar 
amostras dos produtos acabados na linha de produção. Cada amostra contém produtos
defeituosos e não defeituosos representados por 1 e 0, respectivamente.
 Depois de colocar as amostras do produto sequencialmente em uma matriz quadrada bidimensional de amostras do produto,
determine o tamanho da maior área quadrada dos produtos defeituosos.
Exemplo nxn = matriz 5 x 5 de amostras de produto amostras
= [[1,1,1,1,1], [1,1,1,0,0], [1,1,1,0,0], [ 1,1,1,0,0], [1,1,1,1,1]] 1 1 1 1 1 1 1 1 1 111 111 0 0 1 0 0 1 1 1 1 1 1 1 1 0 0 1 1 0 0 1 0 0 1 1 0 0 1 1 jolo 1 1 1 1 1 | 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
A primeira área quadrada dos produtos defeituosos é uma submatriz 3 x 3 começando em (0,0) e terminando em (3,3) •
A segunda área quadrada de produtos defeituosos também é uma submatriz 3 x 3 começando em (1,0) e terminando em (4,
A terceira área quadrada de produtos defeituosos também é uma submatriz 3 x 3 começando em (2,0) e terminando em (5,3) • O tamanho da maior área quadrada de produtos defeituosos é 3 Descrição da Função Complete a função maiorArea no editor abaixo. largeArea tem o seguinte parâmetro: int samples [n] [n]: um array bidimensional de inteiros Returns: int: um inteiro que representa o tamanho da maior submatriz quadrada de produtos defeituosos. Restrições • Osn'''


# Function to find the size of the largest square submatrix of 1's
# Função para encontrar o tamanho da maior submatriz quadrada de 1's
# present in a given binary matrix
# Função para encontrar o tamanho da maior submatriz quadrada de 1's

def findLargestSquare(M):
    # `T [i] [j]` armazena o tamanho da submatriz quadrada máxima terminando em `M [i] [j]`
    T = [[0 for x in range(len(M[0]))] for y in range(len(M))]
    # `max` armazena o tamanho da maior submatriz quadrada de 1's
    max = 0
    # preencher de maneira ascendente para i no intervalo
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[i][j] = M[i][j]
            # se não estivermos na primeira linha ou primeira coluna e o
            # célula atual tem valor 1
            if i > 0 and j > 0 and M[i][j] == 1:
            # a maior submatriz quadrada terminando em `M [i] [j]` será 1 mais
            # mínimo da maior submatriz quadrada terminando em `M [i] [j-1]`,
            # `M [i-1] [j]` e `M [i-1] [j-1]`
                T[i][j] = min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1]) + 1
            # tamanho máximo de atualização encontrado até agora
            if max < T[i][j]:
                max = T[i][j]
            # retorna o tamanho da maior matriz quadrada retorno  máximo
            if max < T[i][j]:
    return max
if __name__ == '__main__':
    # input matrix
    mat = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]

    print("The size of largest square submatrix of 1's is", findLargestSquare(mat))
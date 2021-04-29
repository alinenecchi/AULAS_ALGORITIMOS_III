# Function to find the size of the largest square submatrix of 1's
# Função para encontrar o tamanho da maior submatriz quadrada de 1's
# present in a given binary matrix
# Função para encontrar o tamanho da maior submatriz quadrada de 1's

def findLargestSquare(M):
    # `T[i][j]` stores the size of maximum square submatrix ending at `M[i][j]`
    # `T [i] [j]` armazena o tamanho da submatriz quadrada máxima terminando em `M [i] [j]`
  
    T = [[0 for x in range(len(M[0]))] for y in range(len(M))]

    # `max` stores the size of the largest square submatrix of 1's
    # `max` armazena o tamanho da maior submatriz quadrada de 1's
    max = 0

    # fill in a bottom-up manner
    # preencher de maneira ascendente para i no intervalo
    for i in range(len(M)):
        for j in range(len(M[0])):
            T[i][j] = M[i][j]

            # if we are not at the first row or first column and the
            # current cell has value 1

            # se não estivermos na primeira linha ou primeira coluna e o
            # célula atual tem valor 1

            if i > 0 and j > 0 and M[i][j] == 1:
                # the largest square submatrix ending at `M[i][j]` will be 1 plus
                # minimum of the largest square submatrix ending at `M[i][j-1]`,
                # `M[i-1][j]` and `M[i-1][j-1]

                # a maior submatriz quadrada terminando em `M [i] [j]` será 1 mais
                # mínimo da maior submatriz quadrada terminando em `M [i] [j-1]`,
                # `M [i-1] [j]` e `M [i-1] [j-1]`

                T[i][j] = min(T[i][j - 1], T[i - 1][j], T[i - 1][j - 1]) + 1

            # update maximum size found so far
            # tamanho máximo de atualização encontrado até agora
            
            if max < T[i][j]:
                max = T[i][j]

            # return size of the largest square matrix
            # retorna o tamanho da maior matriz quadrada retorno  máximo
          
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
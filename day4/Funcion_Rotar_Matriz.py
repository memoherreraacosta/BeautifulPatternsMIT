####### AVANZADO
# Crea una funcion que reciba una matriz (listas anidadas) de n x n y la rote a la derecha, sin crear una segunda matriz
"""
Ejemplo:

Matriz
        [[0,2]
         [3,4]]
Matriz Rotada
        [[3,0]
         [4,2]]
"""

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n//2):
        last = n - i - 1
        for j in range(i, last):
            offset = j - i
            top = matrix[i][j]
            matrix[i][j] = matrix[last-offset][i]
            matrix[last-offset][i] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i+offset][last]
            matrix[i+offset][last] = top
    return matrix

n = int(input("Introduce length of array 'n'\n"))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(j)
print(matrix)
rotated = rotate_matrix(matrix)
print(rotated)
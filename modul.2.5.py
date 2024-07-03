def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return


n = int(input('Задайте количество строк : '))
m = int(input('Задайте количество столбцов : '))
value = input(f'Задайте значение : ')
print('' * m)
matrix = get_matrix(n, m, value)
if n <= 0:
    print('Матрица пуста, задано неверное количество строк:', n)
elif m <= 0:
    print('Матрица пуста, задано неверное количество столбцов:', m)
else:
    print('Матрица воплоти')

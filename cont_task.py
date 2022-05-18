import copy
equation_system = []
equation_right = []
num = int(input('Введите количество уравнений в системе - '))

for i in range(num):
    equation_system_row =input(f'Введите коэффициенты уравнения {i+1}, разделяя их пробелами - ').split()
    for i, elem in enumerate(equation_system_row):
        equation_system_row[i] = int(elem)
    equation_system.append(equation_system_row)
for i in range(num):
    equation_right_element = input(f'Введите правую часть уравнения {i+1} - ')
    equation_right_element = float(equation_right_element)
    equation_right.append(equation_right_element)

#Получение минора матрицы
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

#Для матрицы размером 2x2
def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

delta = getMatrixDeternminant(equation_system)
for rows in range(len(equation_system)):
    buffer = copy.deepcopy(equation_system)
    for cols in range(len(equation_system)):
        buffer[cols][rows] = equation_right[cols]
    print(buffer)
    deltaX = getMatrixDeternminant(buffer)
    result = deltaX/delta
    print(f'Неизвестный член №{rows} - ', result)


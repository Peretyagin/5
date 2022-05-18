input_A_rows = int(input("Введите количество уравнений в системе - "))

print("Введите коэффициенты уравнений построчно, разделяя коэффициенты пробелами - ")
inputA = [list(map(float, (input(f"Строка {i + 1} - ").split())))
          for i in range(input_A_rows)]
inputB = map(float, input("Введите матрицу правых частей, разделяя коэффициенты пробелами - ").split())
inputB = list(inputB)


# Перестановка строк
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


# Деление строки на заданный делитель
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


# Сложение строки с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


# Решение системы методом Гаусса
def Gauss(A, B):
    count = 0
    while (count < len(B)):
        current_row = None
        for r in range(count, len(A)):
            if current_row is None or abs(A[r][count]) > abs(A[current_row][count]):
                current_row = r
        if current_row is None:
            print("Решений нет")
            return None
        if current_row != count:
            SwapRows(A, B, current_row, count)
        DivideRow(A, B, count, A[count][count])
        for r in range(count + 1, len(A)):
            CombineRows(A, B, r, count, -A[r][count])
        count += 1
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    print("Ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in
                    enumerate(X)))
    return X


print("Приступаем к вычислениям")
Gauss(inputA, inputB)



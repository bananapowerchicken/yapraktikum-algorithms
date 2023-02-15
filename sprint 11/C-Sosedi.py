# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех
# его соседей. Соседним считается элемент, находящийся от текущего на одну
# ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не 
# считаются.

# ввод данных
m = int(input())  # кол-во строк в матрице
n = int(input())  # кол-во столбцов в матрице

res_arr = []  # неотсортированный массив соседних чисел
input_matrix = []

# ввод двумерного массива
for i in range(m): 
    input_matrix.append(list(map(int, input().split())))

# индексы текущего эл-та
i = int(input())
j = int(input())

# сам алгоритм
if i > 0:
    res_arr.append(input_matrix[i-1][j])
if i < m-1:
    res_arr.append(input_matrix[i+1][j])
if j > 0:
    res_arr.append(input_matrix[i][j-1])
if j < n-1:
    res_arr.append(input_matrix[i][j+1])

# вывод финалочки
res_arr.sort()
print(" ".join(map(str, res_arr)))  # вывод просто всех элементов массива - подходит тренажеру

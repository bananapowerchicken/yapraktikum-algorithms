# Даны два массива чисел длины n. Составьте из них один массив длины 2n,
# в котором числа из входных массивов чередуются (первый — второй — первый 
# — второй — ...). При этом относительный порядок следования чисел из одного
# массива должен быть сохранён.

n = int(input())  # так считывается одно число
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

new_arr = []
for i in range(n):
    new_arr.append(arr1[i])
    new_arr.append(arr2[i])


print(n)
print(arr1)
print(arr2)
print(new_arr)  #  вывод массива
print(" ".join(map(str, new_arr)))  # вывод просто всех элементов массива - подходит тренажеру

# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
# Измерения велись n секунд.
# В секунду i поступает qi запросов.
# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

n = int(input())  #  натуральное число n, количество секунд, в течение которых велись измерения
data = list(map(int, input().split()))  #  n целых неотрицательных чисел
window = int(input())   # натуральное число - окно сглаживания

moving_avg_arr = []

first_sum = sum(data[0:window])
moving_avg_arr.append(first_sum/window)

curr_sum = first_sum
k = window - 1
for i in range(1, len(data)-k):
    curr_sum -= data[i-1]
    curr_sum += data[i+k]
    moving_avg_arr.append(curr_sum/window)

print(" ".join(map(str, moving_avg_arr)))  # вывод просто всех элементов массива - подходит тренажеру
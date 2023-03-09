def calculate_day(num_total, day_sums, b, l_board, r_board):
    # тут где-то должна быть зашита рекурсия - т е ф-я вызывать сама себя
    # а еще сложность дб логарифмическая - т е просто перебор не катит

    # думаю
    # подавать все-таки стоит массив
    # стоит сразу проверять величину посл текущего эл-та
    # типа правая граница будет искать 2 велика
    # а левая - один
    #  сначала лево - это 1ый день, а право - последний
    # потом проверяю границы и двигаю их в середины
    # потом вызываю ту же ф-ю с новыми границами
    res = [-1, -1]
    
    if int(day_sums[r_board]) < b:
        return res
    if int(day_sums[l_board]) >= 2 * b:
        res[0] = res[1] = int(day_sums[l_board])
        return res
    if int(day_sums[l_board]) >= b:
        res[0] = int(day_sums[l_board])




if __name__ == '__main__':
    total_days = int(input())  # общее число дней накапливания
    sum_array = input().split()  # сумма в разные дни
    bike_price = int(input())  # цена одного велосипеда

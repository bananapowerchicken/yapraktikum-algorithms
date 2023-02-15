# Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано
# количество очков. Сначала Гоша называет число k, затем Рита должна выбрать
# две фишки, сумма очков на которых равна заданному числу.
# Рите надоело искать фишки самой, и она решила применить свои навыки
# программирования для решения этой задачи. Помогите ей написать программу для
# поиска нужных фишек.

n = int(input())  #  натуральное число n, количество фишек
fishki = list(map(int, input().split()))  #  сами фишки
target_sum = int(input())   # целевая сумма


# # my own optimization before reading - not naive algo - not good timing( 3.148 ms, 4.15Mb)
# anti_fishki = []

# for i in range(n):
#     anti_fishki.append(target_sum-fishki[i])

# find = False
# for i in range(n-1):
#     for j in range(i+1):
#         if (anti_fishki[j] == fishki[n-i-1+j]):
#             print( target_sum-anti_fishki[j], anti_fishki[j])
#             find = True
#             break
#     if find:
#         break
# if not find:
#     print("None")


find = False
# naive algo - faster the my own - 2.814s, 4.25Mb - more memory
for i in range(n):
    for j in range(i+1, n):
        if fishki[i]==target_sum-fishki[j]:
            print(fishki[i], fishki[j])
            find=True
            break
    if find:
        break
if not find:
    print("None")



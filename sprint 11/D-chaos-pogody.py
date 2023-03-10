# Метеорологическая служба вашего города решила исследовать погоду новым 
# способом.

# Под температурой воздуха в конкретный день будем понимать максимальную
# температуру в этот день.
# Под хаотичностью погоды за n дней служба понимает количество дней, в
# которые температура строго больше, чем в день до (если такой существует)
# и в день после текущего (если такой существует). Например, если за 5 дней
# максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов, то
# хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
# Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

# Заметим, что если число показаний n=1, то единственный день будет хаотичным!

n = int(input())  # количество дней
data = list(map(int, input().split()))  # температура по дням
res = 0  # количество хаотичных дней, искомый результат

# обработка варианта без инфы или с одним лишь днем по условиям
if n < 2:
    print(n)
elif n == 2:
    if data[0] != data[1]:
        res += 1
    print(res)
else:
    if data[0] > data[1]:
        res += 1    
    i = 1 + res 
    while i <= n-1:
        if data[i] > data[i-1] and data[i] > data[i+1]:
            res += 1
            i += 2  # перешагиваю через след значение, т к оно не м б максимумом
        else:
            i += 1
        if i == n-1:
            if data[i] > data[i-1]:
                res += 1                
            break

    print(res)
     
    
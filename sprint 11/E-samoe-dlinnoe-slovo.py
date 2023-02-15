# Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному
# менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо
# оценить сложность статьи.

# Он придумал такой метод оценки: берётся случайное предложение из текста и
# в нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.

# Помогите Гоше справиться с этой задачей.


n = int(input())  # количество дней
text = input()  # строка с текстом


# # A - наивный алгоритм - 	109ms 4.24Mb
# curr_length = 0
# curr_word=""
# max_length = 0
# max_word = ""

# for i in range(n):
#     if text[i] == " ":
#         if curr_length > max_length:
#             max_word = curr_word
#             max_length = curr_length            
#         curr_word=""
#         curr_length = 0
        
#     else:
#         curr_length += 1
#         curr_word += (text[i])

#         if i == n-1 and curr_length > max_length:
#             max_word = curr_word
#             max_length = curr_length  

# print(max_word)
# print(max_length)


# Б - через split  77ms 4.24Mb - готовые решения работают быстрее
max_word = max(text.split(" "), key=len)
max_len = len(max_word)
print(max_word)
print(max_len)
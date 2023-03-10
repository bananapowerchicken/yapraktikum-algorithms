# Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы
# и цифры, заглавные и строчные буквы считаются одинаковыми.

# Решение должно работать за O(N), где N — длина строки на входе.

# Формат ввода
# В единственной строке записана фраза или слово. Буквы могут быть только
# латинские. Длина текста не превосходит 20000 символов.

# Фраза может состоять из строчных и прописных латинских букв, цифр, знаков
# препинания.

# Формат вывода
# Выведите «True», если фраза является палиндромом, и «False», если не является.

text = input()

text = ("".join(c for c in text if c.isalnum())).lower()
n = len(text)

i = 0
while i <= n//2:
    if text[i] != text[n-1-i]:
        print("False")
        break
    i += 1
    if i > n//2: 
        print("True")
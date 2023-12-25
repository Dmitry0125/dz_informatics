# №1
f = input()  # '17-282.txt'
a = [int(x) for x in open(f)]
b = max([x for x in a if x % 41 == 0])  # максимальный элемент последовательности, кратный 41
ans = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) < b:
        ans.append(a[i] + a[i + 1])
print(len(ans), max(ans))

# №2
f = input()  # '17-328.txt'
a = [int(x) for x in open(f)]
b = [x for x in a if x % 2 != 0]  # все нечётные числа в файле
b = sum(b) / len(b)  # среднее арифметическое всех нечётных чисел в файле
ans = []
for i in range(len(a) - 2):
    if ('7' not in (oct(a[i] + a[i + 1])[2:])) and ('7' not in (oct(a[i + 1] + a[i + 2])[2:])) and ('7' not in (oct(a[i] + a[i + 2])[2:])) and (a[i] + a[i + 1] + a[i + 2]) < b:
        ans.append(a[i] + a[i + 1] + a[i + 2])
print(len(ans), max(ans))

# №3
f = '17-341.txt'
a = [int(x) for x in open(f)]
b = sum(a) / len(a)  # среднее арифметическое всех чисел в файле
ans = []  # для "выведите максимальную сумму среди найденных пар"
k = 0  # для "в которых есть хотя бы одно число, большее среднего арифметического всех чисел в файле"
for i in range(len(a) - 3):
    if a[i + 1] * a[i + 2] > a[i] * a[i + 3]:
        ans.append(a[i + 1] + a[i + 2])
        if a[i + 1] > b or a[i + 2] > b:
            k += 1
print(max(ans), k)

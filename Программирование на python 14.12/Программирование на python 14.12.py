# №1
n = int(input())
ch = 2
zn = 1
s = ch/zn
for i in range(2,n+1):
    ch *= 2*i
    zn *= 2*i-1
    s += ch/zn
print(s)
# №2

# №3
n = str(sum(list(map(int,input()))))
# map(int,input()) - строку превратили в массив с элементами строки типа целого числа
while len(n)>1:
    n = str(sum(list(map(int,n))))
print(n)


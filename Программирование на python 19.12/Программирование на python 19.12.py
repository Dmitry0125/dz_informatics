# №1
a = sorted(list(map(int,input().split())))
sr = sum(a)/len(a)
for c in a:
    if c>sr:
        print(c)
        break
# №2
n = int(input())
d = {}
for i in range(n):
    a = int(input())
    if a not in d:
        d[a]=1
    else:
        d[a]+=1
print(d[min(d)], min(d))
# №3
a = list(map(int, input().split()))
ch = []
nch = []
for n in a:
    if n%2==0:
        ch.append(n)
    else:
        nch.append(n)
print(nch+ch)

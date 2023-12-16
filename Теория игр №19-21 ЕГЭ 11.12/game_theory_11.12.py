# №1
m = int(input()) # по условию задачи
z = m # рандомное название переменной, просто для удобства взял другую, т.к. использую m в других целях
def f(s,m):
    if s>=z: return m%2==0
    if m==0: return 0
    h = [f(s+1,m-1),f(s*2,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1,z) if f(s,2)])
print('20)', [s for s in range(1,z) if not f(s,1) and f(s,3)])
print('21)', [s for s in range(1,z) if f(s,4) and not f(s,2)])
# №2
k = int(input())
def f(a,b,m):
    if a==b: return m%2==0
    if m==0: return 0
    if a<b: h = [f(a+1,b,m-1),f(a+3,b,m-1)]
    else: h = [f(a,b+1,m-1),f(a,b+3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print('19)', [s for s in range(1,51) if not f(k,s,1) and f(k,s,2)])
# print('19)', [s for s in range(1,51) if not f(k,s,1) and f(k,s,2)][0]) # вывод как в ответе в задании
print('20)', [s for s in range(1,51) if not f(k,s,1) and f(k,s,3)])
# print('20)', [s for s in range(1,51) if not f(k,s,1) and f(k,s,3)][0],[s for s in range(1,51) if not f(k,s,1) and f(k,s,3)][1]) # вывод как в ответе в задании
print('21)', [s for s in range(1,51) if f(k,s,4) and not f(k,s,2)])
# print('21)', [s for s in range(1,51) if f(k,s,4) and not f(k,s,2)][0],[s for s in range(1,51) if f(k,s,4) and not f(k,s,2)][-1])

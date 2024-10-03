
import copy
from collections import deque
l =[10,20,30,40,50]


print(l)
l.append(60)
print(l)
l.insert(2,25)
print(l)
l.remove(25)
print(l)
t = l.pop()
print(t)
print(l)
l.insert(0,-10)
print(l)
t = l.pop(0)
print(l)

print(50*'-')
l =[10,20,30,40,50]
# l1 = l[:]
l1 = l.copy()
l[0] = 1000
l1[0] = 1000000
l.append('toto')
print(l) # [1000,20,30,40,50]
print(l1) # [1000,20,30,40,50]
print(50*'-')
l=[
    [10,20,30],
    [40,50,60],
    [70,80,90],
]
print(l)
l1 = copy.deepcopy(l)
l[1][1] = 1000
print(l)
print(l1)

print(50*'-')
l =[10,20,30,40,50]

d = deque(l)
l[0] = 1000
d.appendleft(-10)
print(l)
print(d)
d[0] = 2000
print(d)


print(50*'-')

l=[]
for i in range(10,60,10):
    if i>20:
        l.append(i*2)


print(l)

# a=2
l = list(map(lambda i:i,range(10,60,10)))
print(l)

l = [i*2 for i in range(10,60,10) if i>20]
print(l)

lines = [" La ligne1   ","    ligne2\n","La\tligne3\t"]
clean_lines  = [line.strip() for line in lines]
print(lines)
print(clean_lines)
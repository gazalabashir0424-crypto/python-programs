n = int(input())
s = str(n)
p = len(s)
t = 0

for i in s:
    t = t + int(i) ** p

if t == n:
    print("Armstrong")
else:
    print("Not Armstrong")

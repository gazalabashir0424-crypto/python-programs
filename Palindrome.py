n = int(input())
r = 0
t = n

while t > 0:
    d = t % 10
    r = r * 10 + d
    t = t // 10

if r == n:
    print("Palindrome")
else:
    print("Not Palindrome")

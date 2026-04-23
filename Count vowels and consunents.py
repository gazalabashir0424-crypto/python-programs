s = input()
v = "aeiouAEIOU"
vc = 0
cc = 0

for i in s:
    if i.isalpha():
        if i in v:
            vc = vc + 1
        else:
            cc = cc + 1

print(vc)
print(cc)

a = []

num = int(input("num: "))
number = 0
for i in range(1, num + 1):
    number += 1
    e = int(input("num" + str(number) + ":"))
    a.append(e)

print(max(a))
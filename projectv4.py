import time

tic = time.perf_counter()
ab = []

amount = input("how many numbers do you want to sort?")
for e in range(int(amount)):
    numberofTimes = input("enter numbers ")
    ab.append(numberofTimes)
x = len(ab)
for j in range(0, x-1):
    for i in range(0, x-1-j):
        if ab[i] > ab[i+1]:
            temp = ab[i]
            ab[i] = ab[i+1]
            ab[i+1] = temp  
print(ab)
toc = time.perf_counter()vc 
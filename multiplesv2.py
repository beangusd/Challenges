def returnMultiples(num, length):
    multiples = []
    numbers = 0
    for i in range(length):
        numbers += 1
        multiples.append(num * numbers)
        print(multiples)
print(returnMultiples(8, 4))

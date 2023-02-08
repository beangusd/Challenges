def returnSomething(num):
    length = 0
    for i in str(num):
        length += 1
    return length
print(returnSomething(100))
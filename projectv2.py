a = []
largestNumber = 0
num = int(input("enter amount of times to repeat: "))
number = int(input("enter numbers: "))
largestNumber = number
for i in range(2, num + 1):
    number = int(input("enter numbers: "))
    if(largestNumber < number):
        largestNumber = number

print(largestNumber)


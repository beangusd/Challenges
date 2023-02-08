array1 = [1, 2, 3, 4, 5]
target1 = 6

def two_sum(arr, target):
    values = dict()

    for num, numbers in enumerate(arr):
        needed = target - numbers

        if needed in values:
            return [values[needed], num]
    
        values[numbers] = num
    return []
    print(type(values))
print(two_sum(array1, target1))
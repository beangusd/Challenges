arr = [1, 5, 2, 3, 6, 7]
target1 = 9


def two_sum(array, target):
    values = dict()

    for i, elem in enumerate(array):
        compl = target - elem
        if compl in values:
            return [values[compl], i]
        values[elem] = i
        print(i)
        


list1 = two_sum(arr, target1)
print(list1)

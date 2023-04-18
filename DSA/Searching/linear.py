# it's doesn't matter whether the list is sorted or not it will go through all the possible numbers i.e it's linear
arr = [12, 25, 33, 37, 48, 57, 86, 92]


def linearSearch(arr, f):
    n = len(arr)
    index = 0
    for i in range(n):
        if arr[i] == f:
            index = i
    return index


print(linearSearch(arr, 48))


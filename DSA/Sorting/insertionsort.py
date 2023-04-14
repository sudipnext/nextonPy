arr = [57, 25, 48, 37, 12, 92, 86, 33]


def insertionSort(arr):
    for i in range(1, len(arr)):
        value = arr[i]  
        hole = i  
        while hole > 0 and arr[hole-1] > value:  
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = value


insertionSort(arr)
print(arr)

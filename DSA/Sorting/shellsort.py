arr = [25, 57, 48, 37, 12, 92, 86, 33]

def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

shellSort(arr)
print(arr)
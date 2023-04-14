arr = [25, 57, 48, 37, 12, 92, 86, 33]

def merge(left, right, arr):
    lenL = len(left)
    lenR = len(right)
    i = 0
    j = 0
    k = 0
    while i < lenL and j < lenR:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < lenL:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < lenR:
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr):
    n = len(arr)
    if(n < 2):
        return
    mid = n // 2
    leftArr = []
    rightArr = []
    leftArr= arr[:mid]
    rightArr = arr[mid:n]
    mergeSort(leftArr)
    mergeSort(rightArr)
    merge(leftArr, rightArr, arr)


mergeSort(arr)
print(arr)
arr = [25, 57, 48, 37, 12, 92, 86, 33]

def radixsort(arr):
    n = len(arr)
    maxm = getMax(arr)
    i=1
    for i in range(i, maxm, i*10):
        countingSort(arr, i)

def getMax(arr):
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if (arr[i] > max):
            max = arr[i]
    return max

def countingSort(arr, div):
    n = len(arr)
    output = arr.copy()
    r = 10
    count = [0] * r
    for i in range(n):
        count[(arr[i]//div)%10] += 1
    for i in range(1, r):
        count[i] = count[i] + count[i-1]
    for i in range(n-1, -1, -1):
        output[count[(arr[i]//div)%10]-1] = arr[i]
        count[(arr[i]//div)%10] -= 1
    for i in range(n):
        arr[i] = output[i]

radixsort(arr)
print(arr)

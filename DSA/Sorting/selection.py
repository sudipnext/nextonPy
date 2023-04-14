arr = [25, 57, 48, 37, 12, 92, 86, 33]

def selection(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]



selection(arr)
print(arr)
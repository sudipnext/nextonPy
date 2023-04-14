arr = [25, 57, 48, 37, 12, 92, 86, 33]

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            if(arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]


bubblesort(arr)
print(arr)
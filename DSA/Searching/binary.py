# the list need to be sorted in order for binary search to work
arr = [12, 25, 33, 37, 48, 57, 86, 92]
def binarySearch(arr, num):
    def binarySearchHelper(arr, num, low, high):
        #if single element in the array
        if high == low:
            return arr[low] == num
        #finding mid value
        mid = (low+high)//2
        #if the value is at midpoint return true
        if arr[mid] == num:
            return True
        #checking if the midpoint value greater than the number we are searching
        elif arr[mid] > num:
            if low == mid:
                return False
            else:
                return binarySearchHelper(arr, num, low, mid-1)
        else:
            return binarySearchHelper(arr, num, mid+1, high)
    return binarySearchHelper(arr, num, 0, len(arr)-1)

print(binarySearch(arr, 33))
def TOH(n, start, end, middle):
    if (n == 1):
        printHanoi(start, end)
    else:
        TOH(n-1, start, middle, end)
        printHanoi(start, end)
        TOH(n-1, middle, end, start)


def printHanoi(start, end):
    print(f"{start} --> {end}")


n = int(input())

TOH(n, "A", "C", "B")

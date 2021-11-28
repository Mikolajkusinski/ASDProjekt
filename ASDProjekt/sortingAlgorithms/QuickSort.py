import time

from numpy import random

bo = random.randint(100, size=(85000))
arr2 = bo
arr = bo

print(arr)

def partitionRev(arr2, low, high):
    i = (low - 1)
    pivot = arr2[high]

    for j in range(low, high):

        if arr2[j] >= pivot:
            i = i + 1
            arr2[i], arr2[j] = arr2[j], arr2[i]

    arr2[i + 1], arr2[high] = arr2[high], arr2[i + 1]
    return (i + 1)


def quickSortRev(arr2, low, high):
    if len(arr2) == 1:
        return arr2
    if low < high:
        pi = partitionRev(arr2, low, high)

        quickSortRev(arr2, high , pi - 1)
        quickSortRev(arr2, pi + 1, low )


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = len(arr)

start = time.time()
quickSort(arr, 0, n - 1)
end = time.time()
qSTime = end - start

print(arr)
print("Quick sort takes %g seconds to sort array with 85000 elements" %qSTime )

start2 = time.time()
quickSortRev(arr2, 0, n - 1)
end2 = time.time()
revQSTime = end2 - start2

print(arr2)
print("Reverse quick sort takes %g seconds to sort array with 85000 elements" %revQSTime )



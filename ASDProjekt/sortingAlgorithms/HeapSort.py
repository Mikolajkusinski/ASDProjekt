import time

from numpy import random

arr = random.randint(100, size=(85000))

print(arr)

heapSortArr = arr
revHeapSortArr = arr

def heapify(heapSortArr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and heapSortArr[i] < heapSortArr[l]:
        largest = l

    if r < n and heapSortArr[largest] < heapSortArr[r]:
        largest = r

    if largest != i:
        heapSortArr[i], heapSortArr[largest] = heapSortArr[largest], heapSortArr[i]

        heapify(heapSortArr, n, largest)


def heapSort(heapSortArr):
    n = len(heapSortArr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(heapSortArr, n, i)

    for i in range(n - 1, 0, -1):
        heapSortArr[i], heapSortArr[0] = heapSortArr[0], heapSortArr[i]
        heapify(heapSortArr, i, 0)


def revheapify(revHeapSortArr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and revHeapSortArr[l] < revHeapSortArr[smallest]:
        smallest = l

    if r < n and revHeapSortArr[r] < revHeapSortArr[smallest]:
        smallest = r

    if smallest != i:
        (revHeapSortArr[i],
         revHeapSortArr[smallest]) = (revHeapSortArr[smallest],revHeapSortArr[i])

        revheapify(revHeapSortArr, n, smallest)


def revHeapSort(revHeapSortArr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        revheapify(revHeapSortArr, n, i)

    for i in range(n - 1, -1, -1):
        revHeapSortArr[0], revHeapSortArr[i] = revHeapSortArr[i], revHeapSortArr[0]
        revheapify(revHeapSortArr, i, 0)

n = len(arr)

start7 = time.time()
heapSort(heapSortArr)
end7 = time.time()

heapSortTime = end7-start7

print(heapSortArr)
print("Heap sort takes %g seconds to sort array with 85000 elements" %heapSortTime)

start8 = time.time()
revHeapSort(revHeapSortArr,n)
end8 = time.time()

revHeapSortTime = end8-start8

print(revHeapSortArr)
print("Heap sort takes %g seconds to sort array with 85000 elements" %revHeapSortTime)
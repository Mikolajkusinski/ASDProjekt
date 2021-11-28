import time

from numpy import random
randomArr = random.randint(100, size=(85000))



print(randomArr)
print("Tablica poczatkowa")

def bubbleSort(bubbleSortArr):
    n = len(bubbleSortArr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if bubbleSortArr[j] > bubbleSortArr[j + 1]:
                bubbleSortArr[j], bubbleSortArr[j + 1] = bubbleSortArr[j + 1], bubbleSortArr[j]


def revBubbleSort(revBubbleSortArr):
    n = len(revBubbleSortArr)

    for i in range(n - 1):

        for j in range(0, n - i - 1):

            if revBubbleSortArr[j] < revBubbleSortArr[j + 1]:
                revBubbleSortArr[j], revBubbleSortArr[j + 1] = revBubbleSortArr[j + 1], revBubbleSortArr[j]


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

        quickSortRev(arr2, low, pi - 1)
        quickSortRev(arr2, pi + 1, high)


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

def countingSort(countingSortArr):
    maxValue = 0
    for i in range(len(countingSortArr)):
        if countingSortArr[i] > maxValue:
            maxValue = countingSortArr[i]

    buckets = [0] * (maxValue + 1)

    for i in countingSortArr:
        buckets[i] += 1

    i = 0
    for j in range(maxValue+1):
         for a in range(buckets[j]):
             countingSortArr[i] = j
             i += 1

    return countingSortArr

def revCountingSort(revCountingSortArr):
    maxValue = 0
    for i in range(len(revCountingSortArr)):
        if revCountingSortArr[i] > maxValue:
            maxValue = revCountingSortArr[i]

    buckets = [0] * (maxValue + 1)

    for i in revCountingSortArr:
        buckets[i] += 1

    i = 0
    for j in range(maxValue,-1,-1):
         for a in range(buckets[j]):
             revCountingSortArr[i] = j
             i += 1

    return revCountingSortArr

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



n = len(randomArr)

# arr = randomArr.copy()
# start = time.time()
# quickSort(arr, 0, n - 1)
# end = time.time()
# qSTime = end - start
#
# print(arr)
# print("Quick sort takes %g seconds to sort array with 85000 elements" %qSTime )
#
# arr2 = randomArr.copy()
# start2 = time.time()
# quickSortRev(arr2, 0 , n - 1)
# end2 = time.time()
# revQSTime = end2 - start2
#
# print(arr2)
# print("Reverse quick sort takes %g seconds to sort array with 85000 elements" %revQSTime )
#
# bubbleSortArr = randomArr.copy()
# start3 = time.time()
# bubbleSort(bubbleSortArr)
# end3 = time.time()
#
# bubbleSortTime = end3-start3
#
# print(bubbleSortArr)
# print("Bubble sort takes %g seconds to sort array with 85000 elements" %bubbleSortTime)
#
# revBubbleSortArr = randomArr.copy()
# start4 = time.time()
# revBubbleSort(revBubbleSortArr)
# end4 = time.time()
#
# revBubbleSortTime = end4-start4
#
# print(revBubbleSortArr)
# print("Bubble sort takes %g seconds to sort array with 85000 elements" %revBubbleSortTime)

countingSortArr = randomArr.copy()
start5 = time.time()
countingSort(countingSortArr)
end5 = time.time()
countingSortTime = end5 - start5

print(countingSortArr)
print("Counting sort takes %g seconds to sort array with 85000 elements" %countingSortTime)

revCountingSortArr = randomArr.copy()
start6 = time.time()
revCountingSort(revCountingSortArr)
end6 = time.time()
revCountingSortTime = end6 - start6

print(revCountingSortArr)
print("Reverse counting sort takes %g seconds to sort array with 85000 elements" %revCountingSortTime)

heapSortArr = randomArr.copy()
start7 = time.time()
heapSort(heapSortArr)
end7 = time.time()

heapSortTime = end7-start7

print(heapSortArr)
print("Heap sort takes %g seconds to sort array with 85000 elements" %heapSortTime)

revHeapSortArr = randomArr.copy()
start8 = time.time()
revHeapSort(revHeapSortArr,n)
end8 = time.time()

revHeapSortTime = end8-start8

print(revHeapSortArr)
print("Heap sort takes %g seconds to sort array with 85000 elements" %revHeapSortTime)
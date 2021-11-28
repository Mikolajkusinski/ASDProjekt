import time

from numpy import random

arr = random.randint(100, size=(85000))

print(arr)

countingSortArr = arr
revCountingSortArr = arr

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

start5 = time.time()
countingSort(countingSortArr)
end5 = time.time()
countingSortTime = end5 - start5

print(countingSortArr)
print("Counting sort takes %g seconds to sort array with 85000 elements" %countingSortTime)

start6 = time.time()
revCountingSort(revCountingSortArr)
end6 = time.time()
revCountingSortTime = end6 - start6


print(revCountingSortArr)
print("Reverse counting sort takes %g seconds to sort array with 85000 elements" %revCountingSortTime)
import time

from numpy import random

arr = random.randint(100, size=(8500))

print(arr)

bubbleSortArr = arr
revBubbleSortArr = arr


def bubbleSort(bubbleSortArr):
	n = len(bubbleSortArr)

	for i in range(n-1):

		for j in range(0, n-i-1):

			if bubbleSortArr[j] > bubbleSortArr[j + 1] :
				bubbleSortArr[j], bubbleSortArr[j + 1] = bubbleSortArr[j + 1], bubbleSortArr[j]

def revBubbleSort(revBubbleSortArr):
	n = len(revBubbleSortArr)

	for i in range(n-1):

		for j in range(0, n-i-1):

			if revBubbleSortArr[j] < revBubbleSortArr[j + 1] :
				revBubbleSortArr[j], revBubbleSortArr[j + 1] = revBubbleSortArr[j + 1], revBubbleSortArr[j]

start = time.time()
bubbleSort(bubbleSortArr)
end = time.time()

bubbleSortTime = end-start

print(bubbleSortArr)
print("Bubble sort takes %g seconds to sort array with 85000 elements" %bubbleSortTime)

start2 = time.time()
revBubbleSort(revBubbleSortArr)
end2 = time.time()

revBubbleSortTime = end2-start2

print(revBubbleSortArr)
print("Bubble sort takes %g seconds to sort array with 85000 elements" %revBubbleSortTime)


# Insertion sort implementation

import random

from copy import deepcopy

array = [each for each in range(10)]
random.shuffle(array)

def insertion_sort(array=[], ascending=True):
	array = deepcopy(array)
	i, j = 0, 0
	while j < len(array):
		# swaps = 0
		while i < len(array) - 1:
			if ascending:
				expression = array[i] > array[i+1]
			else:
				expression = array[i] < array[i+1]
			if expression:
				# swaps += 1
				array[i], array[i+1] = array[i+1], array[i]
			i += 1
		j += 1
		# print('Pass', j, '-', array, 'Swaps', swaps)
		i = 0
	return array

print('Unsorted', array)
print('Ascending', insertion_sort(array))
print('Descending', insertion_sort(array, False))
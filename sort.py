#Find the minimum and place it in the first position and continue with the remaining of the array
def selection_sort(array):
	c = 0
	while c < len(array):
		minimum = c
		for x in range(c+1,len(array)):
			if array[x] < array[minimum]:
				minimum = x
		temp = array[c]
		array[c] = array[minimum]
		array[minimum] = temp
		c += 1
	return array

#Test
print(selection_sort([1,4,2,3,1,7,2]))

#Push each member of the array to the right as long until finding a bigger one 
def bubble_sort(array):
	n = len(array)
	while n>1:
		mod = True
		i = 0
		while i<n-1:
			if array[i] > array[i+1]:
				temp = array[i]
				array[i] = array[i+1]
				array[i+1] = temp
				mod = False
			i += 1
		if mod:
			break
		else:
			n -= 1
	return array

#Test
print(bubble_sort([1,4,2,3,1,7,2]))

#Insertion sort algorithm
def insertion_sort(array):
	i = 1
	while i < len(array):
		value = array[i]
		j = i-1
		while True:
			if array[j] > value:
				array[j+1] = array[j]
				j -= 1
				if j < 0:
					break
			else:
				break
		array[j+1] = value
		i += 1

	return array


#Test
print(insertion_sort([1,4,2,3,1,7,2]))


#Divide and conquer algorithm
def merge_sort(array):
	if len(array) == 1:
		return array
	else:
		B = array[0 : int(len(array)/2)]
		merge_sort(B)
		C = array[int(len(array)/2) : len(array)]
		merge_sort(C)
		pb = 0
		pc = 0
		while pb+pc < len(array):
			if pb == len(B):
				while pc < len(C):
					array[pb+pc] = C[pc]
					pc += 1
			elif pc == len(C):
				while pb < len(B):
					array[pb+pc] = B[pb]
					pb += 1
			else:
				if B[pb] > C[pc]:
					array[pb+pc] = C[pc]
					pc += 1
				else:
					array[pb+pc] = B[pb]
					pb += 1


		return array

#Test
print(merge_sort([1,4,2,3,1,7,2]))




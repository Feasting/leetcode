
#Key take-aways
	#Inerstion into array is constant since resizing infrequent: O(1)
	#Deleting or Inserting at specific spot: O(n-1)
	#Updating: O(1)

#Write function to put Even in front of array and odd in the back
#Using two pointers to swap
def even_odd(A):
	evenI, oddI = 0, len(A) - 1

	while evenI < oddI:
		#Even, so move even ptr along the array
		if A[evenI] % 2 == 0:
			evenI += 1
		else:
		#Odd, so swap, then move odd ptr to left,
			# since we swapped an odd to that index
			A[evenI], A[oddI] = A[oddI], A[evenI]
			oddI -= 1

#Key methods
	#min(), max(), A.reverse(), reversed(A), A.sort(), sorted(A), del A[i], del A[i:j]



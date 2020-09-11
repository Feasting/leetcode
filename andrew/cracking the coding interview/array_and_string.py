#Array and String

#1.1 isUnique
#O(n)
def isUnique(arr):
	return len(set(arr)) == len(arr)

	#Follow up, no additional datastructures
#O(n^2)
def isUnique2(arr):
	for i in arr:
		for j in arr:
			if i == j:
				return True
	return False

#Test:

#1.2 Check Permutation
#O(nlogn)
def checkPermutation(arr1, arr2):
	return sorted(arr1) == sorted(arr2)
#O(n)
def checkPermutation(arr1, arr2):
	if len(arr1) != len(arr2): return False

	dict1 = {}
	dict2 = {}

	for i in range(len(arr1)):
		if arr1[i] not in dict1:
			dict1[i] = 1
		else:
			dict1[i] += 1

		if arr2[i] not in dict2:
			dict2[i] = 1
		else:
			dict1[i] += 1

	return dict1 == dict2

#Test: print(checkPermutation("addb", "bdad"))

#1.3 URLify

#Split by space and join with "%20"
#O(n)
def URLify(str1):
	list1 = str1.split()
	str1 = list1.join("%20")
	return str1

#O(n)
def URLify2(str1):
	list1 = []
	tempStr = ""
	
	for i in str1:
		if i == " " and tempStr != "":
			list1.append(tempStr)
			tempStr = " "
		elif i != " ":
			tempStr += i 
	
	newString = ""
	for i in range(len(list1)):
		newString += list1[i]
		if i != len(list1) - 1:
			newString += "%20"

	return newString

#1.4 Palindrome Permutation
def isPalindrome(str1):
	return str1[::-1] == str1

#1.5 One Away

#Operations: insert, replace, delete

#O(n)
def oneAway(str1, str2):
	if len(str1) != len(str2) and len(str1) + 1 != len(str2) and len(str1) - 1 != len(str2):
		return False
	else:
		#Check replace
		if len(str1) == len(str2):
			index = -1
			for i in range(len(str1)):
				if str1[i] != str2[i]:
					index = i
			#str1[index] = str2[index]
			str1 = str1[:index] + str2[index] + str1[index + 1:]
			return str1 == str2
		#Check insert
		elif len(str1) + 1 == len(str2):
			index = -1
			for i in range(len(str1)):
				if str1[i] != str2[i]:
					index = i
					break
			#Do the insert
			if index == -1:
			    str1 += str2[-1]
			else:
			    str1 = str1[:index] + str2[index] + str1[index:]
			return str1 == str2 
		#Check delete
		elif len(str2) + 1 == len(str1):
			index = -1
			for i in range(len(str2)):
				if str2[i] != str1[i]:
					index = i
					break
			#Do the insert for second string 
			if index == -1:
			    str2 += str1[-1]
			else:
			    str2 = str2[:index] + str1[index] + str2[index:]
			return str1 == str2

#Test
print("addb", "bdad")
print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))

#1.6 String Compression
#O(n)
def stringCompression(str1):
	original_length = len(str1)

	dict1 = {}

	for i in str1:
		if i not in dict1:
			dict1[i] = 1
		else:
			dict1[i] += 1

	result = ""
	currChar = str1[0]
	count = 0
	for i in str1:
		if i != currChar:
			result += currChar + str(count)
			currChar = i
			count = 1
		else:
			count += 1

	result += currChar + str(count)

	if len(result) < original_length:
		return result
	else:
		return str1

print(stringCompression("aabcccccaaa"))

#1.7 Rotate Matrix
def rotateMatrix(matrix):
	pass

#1.8 Zero Matrix
#O(n^2) or O(n) for traversing the each element of matrix
def zeroMatrix(matrix):
	if not matrix:
		return matrix
	rowsToZero = {}
	colsToZero = {}

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 0:
				rowsToZero.add(row)
				colsToZero.add(col)

	#Set the rows to zero
	for row in rowsToZero:
		for col in range(len(matrix[0])):
			matrix[row][col] = 0

	#Set the cols to zero
	for col in colsToZero:
		for row in range(len(matrix)):
			matrix[row][col] = 0

	return matrix 

#1.9 String Rotation
def isSubstring(str1, str2):
	if str1 in str2:
		return True
	else:
		return False
#O(n) solution
def stringRotation(str1, str2):
	if len(str1) != len(str2):
		return False
	for i in range(len(str1)):
		part1 = str1[:i]
		part2 = str2[i:]
		if isSubstring(part1, str2) and isSubstring(part2, str2):
			return True

	return False
#O(n) solution
def stringRotation(str1, str2):
	if len(str1) != len(str2):
			return False
	for i in range(len(str1)):
		part1 = str1[:i]
		part2 = str2[i:]
		if part2 + part1 == str2:
			return True
	return False

#O(1) solution
def stringRotation(str1, str2):
	if len(str1) != len(str2):
		return False
	if isSubstring(str2, str1 + str1):
		return True
	else:
		return False

print(stringRotation("waterbottle", "erbottlewat"))

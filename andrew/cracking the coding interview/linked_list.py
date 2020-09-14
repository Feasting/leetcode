class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

#Benefit - remove items from beginning in constant time

#Techniques
	#Runner technique


#2.1 Remove Dups

def removeDups(head):
	#With temporary buffer
	set1 = {}
	previous = head
	temp = head
	while temp:
		if temp.val not in set1:
			set1.add(temp.val)
		else:
			#Skip node cause it a repeat
			previous.next = temp.next
		previous = temp
		temp = temp.next

	return head

#Can do another way where we loop linked list twice to check if dups
#O(n^2) solution though

def removeDups2(head):
	#without temporary buffer

#2.2 Return Kth to Last
def findKth(head, k):
	
	dummy = ListNode()
	ptr1 = dummy
	ptr2 = dummy
	dummy.next = head

	#Set ptr2 k nodes apart from ptr1
	for i range(k):
		ptr2 = ptr2.next

	#Loop till ptr2 hits end or None
	while ptr2:
		ptr1 = ptr1.next
		ptr2 = ptr2.next

	return ptr1


#2.3 Delete Middle Node
def deleteMiddleNode(head):

	dummy = ListNode()
	ptr1 = dummy
	ptr2 = dummy
	dummy.next = head

	#Have ptr2 traverse the linked list twice as fast as ptr2
	previous = ptr1
	while ptr2 != None:
		previous = ptr1
		ptr1 = ptr1.next

		if ptr2.next:
			ptr2 = ptr2.next.next
		else:
			ptr2 = ptr2.next

	previous.next = ptr1.next

	#Nothing is returned but the linked list is edited..

#2.4 Partition


#2.5 Sum Lists
def sumLists(node1, node2):
	newList = None
	head = None

	carryOver = 0
	while node1 and node2:
		sum1 = node1.val + node2.val + carryOver
		if sum1 > 10:
			carryOver = 1
			sum1 -= 10
		else:
			carryOver = 0

		#New node
		if newList == None:
			newList = ListNode(sum1)
			head = newList
		else:
			temp = ListNode(sum1)
			newList.next = temp

		node1 = node1.next
		node2 = node2.next

	if node1:
		newList.next = node1
	else:
		newList.next = node2

	return head 

#2.6 Palindrome
def checkPalindrome(head):
	str1 = ""
	
	while head != None:
		str1 += head.val
		head = head.next

	return str1 == str1[::-1]



#2.7 Intersection
#O(n^2) solution loop both linked lists
#O(n) solution - stored nodes of linked list in a set

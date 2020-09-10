"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

19. Remove Nth Node From End of List (Medium)

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if head == None:
            return None
        
        #Use a dictionary to store the indexes of each node
        
        #O(n) traverse list and get length
        #Use the length - n to get what node to remove
        
        dict1 = {}
        
        #Get length of linked list
        length = 0
        temp = head
        while temp:
            dict1[length] = temp
            temp = temp.next
            length += 1
            
        if length == 1:
            return None
        
        #Remove length - n
        #Connect the node before to the node after
        if length - n - 1 < 0:
            return head.next
        else:
            dict1[length - n - 1].next = dict1[length - n].next
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #[1,2], 2
        #Two pointers, set n nodes apart from itself
        #Start before linked list starts
        dummy = ListNode()
        dummy.next = head
        ptr1 = dummy
        ptr2 = dummy
        
        for i in range(n + 1):
            ptr2 = ptr2.next
        
        while ptr2 != None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = ptr1.next.next

        return dummy.next
"""

https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists (Easy)

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        newNode = None
        head = None
        
        while l1 != None and l2 != None:
            
            if l1.val <= l2.val:
                if newNode != None:
                    newNode.next = l1
                    newNode = newNode.next
                else:
                    head = l1
                    newNode = head
                    
                l1 = l1.next
            else:
                if newNode != None:
                    newNode.next = l2
                    newNode = newNode.next
                else:
                    head = l2
                    newNode = head
                l2 = l2.next
                
        if l1 != None:
            newNode.next = l1
        else:
            newNode.next = l2
        
        return head
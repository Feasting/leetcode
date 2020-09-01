"""

https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        newHead = None
        
        while head != None:
            temp = newHead
            #Setting new front node
            newHead = head
            #Traversing Linked List
            head = head.next
            #Creating new linked list
            newHead.next = temp
            
        return newHead
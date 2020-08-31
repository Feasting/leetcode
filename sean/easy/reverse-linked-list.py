# 8-31-2020
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None

        def helper(previous, current):
            if current == None:
                return previous
            temp = current.next
            current.next = previous
            return helper(current, temp)
        
        temp = head.next
        head.next = None
            
        return helper(head, temp)

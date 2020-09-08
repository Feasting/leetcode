# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        newPrev = None
        curr = head
        currNext = curr.next
                
        while currNext:
            curr.next = newPrev
            newPrev = curr
            curr = currNext
            currNext = currNext.next
        
        curr.next = newPrev
        return curr
        
# https://leetcode.com/problems/reverse-linked-list/

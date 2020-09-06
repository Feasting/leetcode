# 9-6-2020
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or k == 0:
            return head
        
        size = 1
        p = head
        while p.next:
            size += 1
            p = p.next
        p.next = head
        p = head
        k %= size
        k = size - k
        for i in range(k - 1):
            p = p.next
        head = p.next
        p.next = None
        return head

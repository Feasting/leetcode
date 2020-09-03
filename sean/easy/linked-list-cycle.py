# 9-2-2020
# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        while p:
            if not p.val:
                return True
            else:
                p.val = None
                p = p.next
        return False

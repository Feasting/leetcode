# 9-1-2020
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        p1 = l1
        p2 = l2
        result = None
        p = None
        if p1.val < p2.val:
            p = p1
            p1 = p1.next
        else:
            p = p2
            p2 = p2.next
        result = p
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        else:
            p.next = p2
        return result

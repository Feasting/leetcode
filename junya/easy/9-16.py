# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode()
        head = curr
        
        while l1 or l2:
            temp = ListNode()
            if l1 is None:
                temp.val = l2.val
                curr.next = temp
                curr = curr.next
                l2 = l2.next
            elif l2 is None:
                temp.val = l1.val
                curr.next = temp
                curr = curr.next
                l1 = l1.next
            else:
                if l1.val > l2.val:
                    temp.val = l2.val
                    curr.next = temp
                    curr = curr.next
                    l2 = l2.next
                else:
                    temp.val = l1.val
                    curr.next = temp
                    curr = curr.next
                    l1 = l1.next
        return head.next
        
# https://leetcode.com/problems/merge-two-sorted-lists/

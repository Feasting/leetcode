# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        
        if l1 == None:
            result = l2
            l2 = l2.next
        elif l2 == None:
            result = l1
            l1 = l1.next
        else:
            if l1.val < l2.val:
                result = l1
                l1 = l1.next
            else:
                result = l2
                l2 = l2.next
        
        tmp = result
        
        while l1 != None or l2 != None:
            # print("l1: " + str(l1.val))
            # print("l2: " + str(l2.val))
            if l1 == None:
                tmp.next = l2
                l2 = l2.next
            elif l2 == None:
                tmp.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    tmp.next = l1
                    l1 = l1.next
                else:
                    tmp.next = l2
                    l2 = l2.next
            
            tmp = tmp.next
            
        return result
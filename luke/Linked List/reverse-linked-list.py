# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr = head
        if ptr is None:
             return None
        while ptr.next != None:
            ptr = ptr.next
        
        def reverseListHelp(node):
            temp = node
            if node.next != None:
                node = reverseListHelp(temp.next)
                temp.next = None
                node.next = temp
                
            return temp
        
        reverseListHelp(head)
        
        return ptr
"""

https://leetcode.com/problems/reorder-list/

143. Reorder List (Medium)

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        
        #Create two lists each have half the linked list
        #Use these two lists to create the new combined linked list
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1
        
        
        list1 = []
        list2 = []
        
        if length % 2 == 0:
            length = length // 2
        else:
            length = length // 2 + 1 
        
        temp = head
        
        for i in range(0, length):
            list1.append(temp)
            temp = temp.next
        
        while temp != None:
            list2.append(temp)
            temp = temp.next
        
        node = list1.pop(0)
        node.next = None
        nodeHead = node
        l1 = False
        while list1 != [] or list2 != []:
            if l1:
                node.next = list1.pop(0)
                node = node.next
                node.next = None
                l1 = False
            else:
                node.next = list2.pop()
                node = node.next
                node.next = None
                l1 = True
        
        return nodeHead
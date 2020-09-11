"""

https://leetcode.com/problems/rotate-list/

61. Rotate List (Medium)

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""


#O(n) solution ~~~

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        #Edge
        if not head:
            return head
        
        temp = head
        count = 1
        #Set temp to last node
        while temp.next != None:
            temp = temp.next
            count += 1
            
        #Use the number k to compute a value k
        if k > count:
            k %= count
        
        dummy = ListNode()
        ptr1 = dummy
        ptr2 = dummy
        dummy.next = head
        
        for i in range(k):
            ptr2 = ptr2.next
        
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        #Do the rotation
        oldHead = head
            #Move sub linked list from end to front
        head = ptr1.next
            #connect old front to end of new front
        ptr2.next = oldHead
        ptr1.next = None
        
        return head
"""

https://leetcode.com/problems/linked-list-cycle/

141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where the tail connects to. If pos == -1, then there is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        #Tortise and hare algorithm
        #have one pointer slowly move across linked list
        #have another point move quickly over
        
        #if pointers equal then cycle
        if head == None:
            return False
        
        tortise = head
        hare = head
        
        while True:
            #hare double step
            if hare.next != None and hare.next.next != None:
                hare = hare.next.next
            else:
                break
            
            #turtle one step
            if tortise.next != None:
                tortise = tortise.next
            else:
                break
            
            if hare.val == tortise.val:
                return True
        
        return False
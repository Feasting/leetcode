#include<iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *turtle = head;
        ListNode *rabbit = head;
        while(turtle != NULL && rabbit != NULL) {
            turtle = turtle->next;
            rabbit = rabbit->next;
            if(rabbit != NULL) {
                rabbit = rabbit->next;
            }
            else {
                return false;
            }
            if(rabbit != NULL && turtle->val == rabbit->val) {
                return true;
            }
        }
        
        return false;
    }
};
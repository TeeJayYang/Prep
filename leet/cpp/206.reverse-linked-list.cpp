/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return head;
        ListNode* prev = nullptr;
        ListNode* next;
        do {
            next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        } while (head);
        return prev;
    }
};

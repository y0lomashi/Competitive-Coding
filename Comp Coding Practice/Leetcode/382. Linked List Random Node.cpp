
// Reservoir sampling R-Algorithm
// https://en.wikipedia.org/wiki/Reservoir_sampling
// Used for selecting random item from undefined size group



Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode *head = NULL;
    Solution(ListNode* head) {
        this->head = head;
    }
    
    int getRandom() {
        int k = 1, res = 0;
        ListNode *curr = this->head;
        while (curr != NULL)
        {
            if (rand() % k == 0)
            {
                res = curr->val;
            }
            k++;
            curr = curr->next;
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
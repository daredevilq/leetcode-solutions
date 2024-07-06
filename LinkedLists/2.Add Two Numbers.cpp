// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */


struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {};
    ListNode(int x) : val(x), next(nullptr) {};
    ListNode(int x, ListNode *next) : val(x), next(next){};
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* current = head;
        int sum = 0;
        while (l1 != nullptr && l2 != nullptr)
        {
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;
            sum += x + y;
            current->next = new ListNode(sum % 10);
            sum = sum  / 10;
            
            current = current->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        

        while(l1 != nullptr){
            sum += l1 ? l1->val : 0;
            current->next = new ListNode(sum%10);
            sum = sum / 10;
            l1 = l1 ? l1->next : nullptr;
            current = current->next;

        }


        while(l2 != nullptr){
            sum += l2 ? l2->val : 0;

            current->next = new ListNode(sum%10);
            sum = sum / 10;
            l2 = l2 ? l2->next : nullptr;
            current = current->next;
        }

        if(sum != 0){
            current->next = new ListNode(sum%10);
        }

        return head->next;

    }
};
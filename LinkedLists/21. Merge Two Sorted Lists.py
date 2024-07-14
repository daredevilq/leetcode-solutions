# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        pointer = head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                pointer.next = list1
                pointer = pointer.next
                list1 = list1.next
            else:
                pointer.next = list2
                pointer = pointer.next
                list2 = list2.next

        if list1 == None:
            pointer.next = list2

        else:
            pointer.next = list1
        
        return head.next


        
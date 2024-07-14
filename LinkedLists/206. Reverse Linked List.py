# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        
        if head.next == None:
            return head

        prev = None
        curr = head
        
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev


def print_list(node):

    head = node

    while head != None:
        print(head.val)
        head = head.next


first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

sol = Solution()



print_list(sol.reverseList(first))
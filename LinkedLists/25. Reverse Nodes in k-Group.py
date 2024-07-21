# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        
        if head == None:
            return None

        pointer = head
        n = 1
        while pointer.next != None:
            n += 1
            pointer = pointer.next
        
        times = n // k

        prev = None
        curr = head
        nex = head.next

        while True:
            

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        
        reversed_values = []
        iterator = 1
        start = head
        pointer = head


        while right >= iterator and pointer != None:
            if iterator >= left:
                reversed_values.append(pointer.val)
            iterator +=1
            pointer = pointer.next
        
        iterator = 1

        res = None
        pointer2 = None
        if left == 1:
            for i in range(len(reversed_values) - 1, -1, -1):
                if res == None:
                    pointer2 = ListNode(reversed_values[i])
                    res = pointer2
                else:
                    pointer2.next = ListNode(reversed_values[i])
                    pointer2 = pointer2.next
            pointer2.next = pointer

            return res
        else:
            res = head
            pointer2 = head
            iterator = 1
            while iterator != left - 1:
                pointer2 = pointer2.next
                iterator +=1

            for i in range(len(reversed_values) - 1, -1, -1):
                pointer2.next = ListNode(reversed_values[i])
                pointer2 = pointer2.next
            pointer2.next = pointer

            return res


def create_linked_list(arr):
    head = ListNode(arr[0])
    pointer = head
    for i in range(1, len(arr)):
        pointer.next = ListNode(arr[i])
        pointer = pointer.next

    return head


def print_list(head):
    pointer = head
    while pointer != None:
        print(pointer.val)
        pointer= pointer.next

head = [1,2,3,4,5,6]
left = 4
right = 6
llist = create_linked_list(head)

sol = Solution()
result = sol.reverseBetween(llist, left, right)

print_list(result)


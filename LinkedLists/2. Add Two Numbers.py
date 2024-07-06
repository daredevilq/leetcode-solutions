# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        number1 = ""
        number2 = ""

        while l1 != None:
            number1 += (str(l1.val))
            l1 = l1.next
    
        while l2 != None:
            number2 += (str(l2.val))
            l2 = l2.next

        number1 = number1[::-1]
        number2 = number2[::-1]  
        
        return int(number1) + int(number2)
    


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = None
        pointer = None
        sum = 0

        while l1 != None and l2 != None:
            sum += l1.val + l2.val
            if head == None:
                head = ListNode(sum%10)
                pointer = head

            else:
                node = ListNode(sum%10)
                pointer.next = node
                pointer = pointer.next

            sum //= 10

            l1 = l1.next
            l2 = l2.next
        

        while l1 != None:
            sum += l1.val
            node = ListNode(sum%10)
            pointer.next = node
            pointer = pointer.next

            sum //= 10
            l1 = l1.next

        while l2 != None:
            sum += l2.val
            node = ListNode(sum%10)
            pointer.next = node
            pointer = pointer.next

            sum //= 10
            l2 = l2.next

        if(sum != 0):
            pointer.next = ListNode(sum)

        return head
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        temp = head
        even_head = head.next
        even = even_head
        while even is not None and even.next is not None:
            temp.next = temp.next.next
            temp = temp.next
            even.next = even.next.next
            even = even.next
        temp.next = even_head
        return head
            
              
        
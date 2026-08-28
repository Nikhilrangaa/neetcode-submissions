# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        temp = head
        first_half = head
        while temp is not None:
            length += 1
            temp = temp.next
        for i in range((length -1) // 2):
            first_half = first_half.next
        second_half = first_half.next
        first_half.next = None
        
        prev = None
        while second_half is not None:
            after = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = after
        
        first = head
        second = prev
        while first is not None and second is not None:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next

        







        


        



        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        curr = head
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next
        
        iterate = length - n
        prev = None

        for i in range(iterate):
            prev = temp
            temp = temp.next
    

        if prev == None:
            return head.next

        prev.next = temp.next
        temp.next = None
        return head




        


        

        